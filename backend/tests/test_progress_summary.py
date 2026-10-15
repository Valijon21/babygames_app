import pytest
from rest_framework.test import APIClient
from apps.accounts.models import User
from apps.child_profiles.models import ChildProfile
from apps.catalog.models import GameCategory, Game
from apps.progress.models import ProgressRecord
from apps.game_sessions.models import GameSession


@pytest.mark.django_db
class TestProgressSummary:
    def setup_method(self):
        self.client = APIClient()
        self.guardian = User.objects.create_user(
            username='guardian_sum', email='guardian_sum@bolajon.uz', password='Pass123!Password'
        )
        self.stranger = User.objects.create_user(
            username='stranger_sum', email='stranger_sum@bolajon.uz', password='Pass123!Password'
        )

        self.child = ChildProfile.objects.create(
            guardian=self.guardian,
            display_name='Jasur',
            age_band='4-5'
        )

        self.category = GameCategory.objects.create(
            slug='colors',
            title='Ranglar',
            sort_order=1
        )
        self.game = Game.objects.create(
            category=self.category,
            slug='magic-coloring',
            title='Sehrli Bo‘yash',
            min_age=3,
            max_age=6,
            status='published'
        )

    def test_progress_summary_for_guardian(self):
        # Create progress records and sessions
        ProgressRecord.objects.create(
            child_profile=self.child,
            game=self.game,
            completed_count=3,
            best_score=3
        )
        GameSession.objects.create(
            child_profile=self.child,
            game=self.game,
            status='completed',
            duration_seconds=120,
            score=3
        )

        self.client.force_authenticate(user=self.guardian)
        response = self.client.get(f'/api/v1/progress/children/{self.child.id}/summary/')

        assert response.status_code == 200
        data = response.data
        assert data['child_id'] == str(self.child.id)
        assert data['display_name'] == 'Jasur'
        assert data['total_games_played'] == 3
        assert data['total_stars'] == 3
        assert data['total_sessions_completed'] == 1
        assert data['total_play_time_seconds'] == 120
        assert len(data['category_breakdown']) == 1
        assert data['category_breakdown'][0]['category_slug'] == 'colors'
        assert len(data['recent_activity']) == 1
        assert data['recent_activity'][0]['game_slug'] == 'magic-coloring'

    def test_progress_summary_forbidden_for_stranger(self):
        self.client.force_authenticate(user=self.stranger)
        response = self.client.get(f'/api/v1/progress/children/{self.child.id}/summary/')

        assert response.status_code == 403
        assert response.data['error']['code'] == 'FORBIDDEN'
