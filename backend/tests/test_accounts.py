from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class AccountsAPITests(TestCase):
    def test_guardian_registration_and_login(self):
        register_url = reverse('auth-register')
        payload = {
            'email': 'parent@example.com',
            'password': 'StrongPassword123!',
            'password_confirm': 'StrongPassword123!',
            'first_name': 'Dilnoza',
            'last_name': 'Karimova'
        }
        response = self.client.post(register_url, payload, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['email'], 'parent@example.com')
        self.assertTrue(response.json()['is_guardian'])

        # Check me endpoint while authenticated
        me_url = reverse('auth-me')
        me_resp = self.client.get(me_url)
        self.assertEqual(me_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(me_resp.json()['email'], 'parent@example.com')

    def test_registration_password_mismatch(self):
        register_url = reverse('auth-register')
        payload = {
            'email': 'fail@example.com',
            'password': 'StrongPassword123!',
            'password_confirm': 'DifferentPassword123!',
        }
        response = self.client.post(register_url, payload, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['error']['code'], 'VALIDATION_ERROR')
