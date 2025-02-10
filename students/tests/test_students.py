from users.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from students.models import Student
import base64


class StudentAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="testpassword",
            first_name="Test",
            last_name="User",
        )
        self.superuser = User.objects.create_superuser(
            email="admin@example.com",
            password="adminpassword",
            first_name="Admin",
            last_name="User",
        )

        self.student = Student.objects.create(
            user=self.user,
            birth_date="2000-01-01",
            phone="1234567890",
            genre="MALE",
            category="BEGINNER",
            profile_img=base64.b64encode(b"testimage").decode("utf-8"),
            frequency_of_classes="2X",
            playing_side="LEFT",
        )

        self.client.force_authenticate(user=self.user)

    def test_create_student(self):
        """Test creating a student"""
        data = {
            "birth_date": "1995-05-10",
            "phone": "9876543210",
            "genre": "FEMALE",
            "category": "INTERMEDIARY",
            "profile_img": base64.b64encode(b"sampleimage").decode("utf-8"),
            "frequency_of_classes": "3X",
            "playing_side": "RIGHT",
        }
        response = self.client.post(reverse("create-students"), data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["user"]["email"], self.user.email)

    def test_get_student_list(self):
        """Test retrieving the list of students for authenticated user"""
        response = self.client.get(reverse("create-students"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
