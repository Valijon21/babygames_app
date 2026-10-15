import pytest
from django.core.exceptions import ValidationError
from rest_framework.test import APIClient
from apps.accounts.models import User
from apps.catalog.models import GameCategory, Game
from apps.game_content.models import ContentAuditEvent
from apps.game_content.validators import validate_asset_payload


@pytest.mark.django_db
class TestContentWorkflowAndAssets:
    def setup_method(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            username='admin_content', email='admin_content@bolajon.uz', password='Pass123!Password'
        )
        self.regular_user = User.objects.create_user(
            username='user_content', email='user_content@bolajon.uz', password='Pass123!Password'
        )
        self.category = GameCategory.objects.create(slug='alphabet', title='Alifbo')
        self.game = Game.objects.create(
            category=self.category,
            slug='uzbek-abc',
            title='O‘zbek Alifbosi',
            status='draft'
        )

    def test_lifecycle_workflow_transitions(self):
        # 1. Draft to review
        self.game.submit_for_review(user=self.admin_user)
        assert self.game.status == 'review'
        assert ContentAuditEvent.objects.filter(game=self.game, action='status_change').count() == 1

        # 2. Review to published
        self.game.publish(user=self.admin_user)
        assert self.game.status == 'published'
        assert self.game.content_version == 2
        assert self.game.published_at is not None

        # 3. Version bump
        self.game.bump_version(user=self.admin_user, reason="Audio yangilandi")
        assert self.game.content_version == 3

        # 4. Archive
        self.game.archive(user=self.admin_user)
        assert self.game.status == 'archived'

    def test_preview_endpoint_permissions(self):
        # Draft game not visible in public game-detail
        pub_response = self.client.get(f'/api/v1/games/{self.game.slug}/')
        assert pub_response.status_code == 404

        # Regular user cannot preview
        self.client.force_authenticate(user=self.regular_user)
        preview_forbidden = self.client.get(f'/api/v1/games/{self.game.slug}/preview/')
        assert preview_forbidden.status_code == 403

        # Staff admin can preview
        self.client.force_authenticate(user=self.admin_user)
        preview_ok = self.client.get(f'/api/v1/games/{self.game.slug}/preview/')
        assert preview_ok.status_code == 200
        assert preview_ok.data['slug'] == 'uzbek-abc'

    def test_asset_size_and_extension_validation(self):
        # Over-sized SVG (exceeds 2MB)
        with pytest.raises(ValidationError):
            validate_asset_payload('svg', 'test.svg', file_size=3 * 1024 * 1024)

        # Disallowed extension for SVG
        with pytest.raises(ValidationError):
            validate_asset_payload('svg', 'test.exe', file_size=500)

        # Invalid XML/SVG bytes
        with pytest.raises(ValidationError):
            validate_asset_payload('svg', 'test.svg', file_size=500, content_bytes=b'not xml')

        # Valid SVG
        valid_svg = (
            b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
            b'<circle cx="50" cy="50" r="40"/></svg>'
        )
        validate_asset_payload('svg', 'test.svg', file_size=len(valid_svg), content_bytes=valid_svg)

        # Valid JSON
        valid_json = b'{"type": "coloring", "regions": []}'
        validate_asset_payload('json', 'schema.json', file_size=len(valid_json), content_bytes=valid_json)
