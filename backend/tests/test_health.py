from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class HealthCheckTests(TestCase):
    def test_health_check_returns_healthy(self):
        url = reverse('health-check')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['status'], 'healthy')
        self.assertEqual(response.json()['database'], 'ok')
        self.assertEqual(response.json()['service'], 'bolajon-api')
        self.assertIn('X-Request-ID', response.headers)
        self.assertTrue(len(response.headers['X-Request-ID']) > 10)
