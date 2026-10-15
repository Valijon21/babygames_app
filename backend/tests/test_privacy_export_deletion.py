import pytest
from rest_framework.test import APIClient
from apps.accounts.models import User
from apps.child_profiles.models import ChildProfile
from apps.catalog.models import GameCategory, Game
from apps.progress.models import ProgressRecord
from apps.game_sessions.models import GameSession


@pytest.mark.django_db
class TestPrivacyExportAndDeletion:
    def setup_method(self):
        self.client = APIClient()
        self.guardian = User.objects.create_user(
            username='parent_coppa', email='parent_coppa@bolajon.uz', password='Pass123!Password'
        )
        self.stranger = User.objects.create_user(
            username='stranger_coppa', email='stranger_coppa@bolajon.uz', password='Pass123!Password'
        )

        self.child = ChildProfile.objects.create(
            guardian=self.guardian,
            display_name='Malika',
            age_band='5-6'
        )

        category = GameCategory.objects.create(slug='memory', title='Xotira')
        self.game = Game.objects.create(category=category, slug='animal-match', title='Hayvonlar', status='published')

        GameSession.objects.create(
            child_profile=self.child,
            game=self.game,
            status='completed',
            duration_seconds=95,
            score=3
        )
        ProgressRecord.objects.create(
            child_profile=self.child,
            game=self.game,
            completed_count=2,
            best_score=3
        )

    def test_export_child_data_portability(self):
        self.client.force_authenticate(user=self.guardian)
        response = self.client.get(f'/api/v1/children/{self.child.id}/export/')

        assert response.status_code == 200
        data = response.data
        assert 'compliance' in data
        assert data['child_profile']['id'] == str(self.child.id)
        assert data['child_profile']['display_name'] == 'Malika'
        assert data['game_sessions_count'] == 1
        assert data['progress_records_count'] == 1
        assert data['game_sessions'][0]['game_slug'] == 'animal-match'

    def test_export_forbidden_for_other_user(self):
        self.client.force_authenticate(user=self.stranger)
        response = self.client.get(f'/api/v1/children/{self.child.id}/export/')
        # get_queryset filter excludes other guardians' children, returning 404
        assert response.status_code == 404

    def test_soft_delete_child_profile(self):
        self.client.force_authenticate(user=self.guardian)
        response = self.client.delete(f'/api/v1/children/{self.child.id}/')

        assert response.status_code == 204
        self.child.refresh_from_db()
        assert not self.child.is_active

    def test_hard_delete_permanent_erasure_coppa(self):
        self.client.force_authenticate(user=self.guardian)
        response = self.client.delete(f'/api/v1/children/{self.child.id}/?hard_delete=true')

        assert response.status_code == 200
        assert response.data['erased'] is True
        assert not ChildProfile.objects.filter(id=self.child.id).exists()
        assert not GameSession.objects.filter(child_profile_id=self.child.id).exists()
        assert not ProgressRecord.objects.filter(child_profile_id=self.child.id).exists()
