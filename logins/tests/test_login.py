from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from users.models import User


class LoginAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse("login")
        self.refresh_url = reverse("refresh_token")

        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="password123",
            first_name="Test",
            is_student=False,
        )

    def test_login_success(self):
        """Login test successful"""
        response = self.client.post(
            self.login_url,
            {"email": "testuser@example.com", "password": "password123"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access_token", response.data)
        self.assertIn("refresh_token", response.data)
        self.assertEqual(response.data["email"], "testuser@example.com")
        self.assertEqual(response.data["is_student"], False)

    def test_login_invalid_credentials(self):
        """Test failed login with invalid credentials"""
        response = self.client.post(
            self.login_url,
            {"email": "testuser@example.com", "password": "wrongpassword"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["detail"], "Invalid credentials")

    def test_login_missing_credentials(self):
        """Test for failed login without credentials"""
        response = self.client.post(self.login_url, {}, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["detail"], "Email and password are required")
