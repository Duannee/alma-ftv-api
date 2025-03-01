from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

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

    def test_create_user_with_invalid_email_fails(self):
        """Test if user creation failed when providing an invalid email"""
        payload = {
            "first_name": "test",
            "last_name": "tests",
            "email": "test.com",
            "password": "testpassword123",
            "is_student": False,
        }
        response = self.client.post(self.register_url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)
        self.assertFalse(User.objects.filter(email=payload["email"]).exists())

    def test_user_password_is_hashed(self):
        """Tests whether the user's password is stored in hashed form"""
        response = self.client.post(self.register_url, self.valid_payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(email=self.valid_payload["email"])
        self.assertTrue(user.check_password(self.valid_payload["password"]))

    def test_user_creation_with_groups_and_permissions(self):
        """Tests whether a user can be created with associated groups and permissions"""
        from django.contrib.auth.models import Group, Permission

        group = Group.objects.create(name="TestGroup")
        permission = Permission.objects.first()

        payload = {
            "first_name": "test",
            "last_name": "tests",
            "email": "test@example.com",
            "password": "testpassword123",
            "is_student": False,
            "groups": [group.id],
            "user_permissions": [permission.id],
        }
        response = self.client.post(self.register_url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(email=payload["email"])
        self.assertIn(group, user.groups.all())
        self.assertIn(permission, user.user_permissions.all())
