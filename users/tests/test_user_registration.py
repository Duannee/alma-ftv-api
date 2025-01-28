from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from users.models import User


class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("register")
        self.valid_payload = {
            "first_name": "test",
            "last_name": "tests",
            "email": "test@example.com",
            "password": "testpassword123",
            "is_student": False,
        }

    def test_register_user_successfully(self):
        """Tests whether a user is created successfully by providing valid data"""
        response = self.client.post(self.register_url, self.valid_payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        self.assertEqual(response.data["email"], self.valid_payload["email"])
        self.assertTrue(User.objects.filter(email=self.valid_payload["email"]).exists())

    def test_create_user_without_email_fails(self):
        """Tests whether user creation fails when email is not provided"""
        payload = {
            "first_name": "test",
            "last_name": "tests",
            "password": "testpassword123",
            "is_student": False,
        }
        response = self.client.post(self.register_url, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)
        self.assertFalse(User.objects.filter(first_name=payload["first_name"]).exists())

    def test_create_user_without_password_fails(self):
        """Tests whether user creation fails when password is not provided"""
        payload = {
            "first_name": "test",
            "last_name": "tests",
            "email": "test@example.com",
            "is_student": False,
        }
        response = self.client.post(self.register_url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)
        self.assertFalse(User.objects.filter(email=payload["email"]).exists())

    def test_create_user_with_existing_email_fails(self):
        """Tests whether user creation fails when trying to use an existing email"""
        User.objects.create_user(email="test@example.com", password="testpassword123")
        response = self.client.post(self.register_url, self.valid_payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)
