from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from apps.accounts.models import User
from apps.child_profiles.models import ChildProfile


class ChildProfileSecurityTests(TestCase):
    def setUp(self):
        self.guardian_a = User.objects.create_user(email='parent_a@example.com', password='Password123!')
        self.guardian_b = User.objects.create_user(email='parent_b@example.com', password='Password123!')

        self.child_a = ChildProfile.objects.create(
            guardian=self.guardian_a,
            display_name='Jasurbek',
            age_band='5-7',
            avatar_key='avatar_fox'
        )

    def test_guardian_cannot_access_other_child_profile(self):
        """Verify strict IDOR prevention: Guardian B cannot see Guardian A's child."""
        self.client.force_login(self.guardian_b)
        url = reverse('child-profile-detail', kwargs={'pk': self.child_a.id})
        response = self.client.get(url)
        # Should return 404 because get_queryset filters by self.request.user
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_guardian_can_crud_own_child(self):
        self.client.force_login(self.guardian_a)
        url = reverse('child-profile-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['results']), 1)
        self.assertEqual(response.json()['results'][0]['display_name'], 'Jasurbek')
