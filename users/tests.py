from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import Profile

class RegisterUserTests(APITestCase):

    def setUp(self):
        self.url = reverse('register') 
        self.valid_payload = {
            "username": "kiera",
            "email": "kiera@example.com",
            "password": "supersecure123"
        }
        self.invalid_payload = {
            "username": "",
            "email": "not-an-email",
            "password": ""
        }

    def test_register_user_success(self):
        """It should create a new user and profile"""
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='kiera').exists())
        user = User.objects.get(username='kiera')
        self.assertTrue(Profile.objects.filter(user=user).exists())

    def test_register_user_invalid_data(self):
        """It should return 400 for invalid data"""
        response = self.client.post(self.url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
        self.assertIn('password', response.data)

    def test_register_duplicate_user(self):
        """It should not allow duplicate usernames"""
        User.objects.create_user(username="kiera", email="already@used.com", password="pass123")
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
