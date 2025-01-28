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
