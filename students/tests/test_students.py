import base64

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from students.models import Student
from users.models import User


class StudentAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="testuser@example.com",
            password="testpassword",
            first_name="Test",
            last_name="User",
            is_student=True,
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

    def test_create_student_fails_if_already_exists(self):
        """Test creating a student fails if the profile already exists"""
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

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)

    def test_get_student_list(self):
        """Test retrieving the list of students for authenticated user"""
        response = self.client.get(reverse("create-students"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_student_detail(self):
        """Test retrieving details of a specific student"""
        url = reverse(
            "retrieve-update-destroy-students", kwargs={"pk": self.student.id}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.student.id)

    def test_update_student(self):
        """Test updating a student's phone number"""
        data = {"phone": 1112223333}
        response = self.client.patch(
            reverse("retrieve-update-destroy-students", args=[self.student.id]),
            data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student.refresh_from_db()
        self.assertEqual(self.student.phone, "1112223333")

    def test_delete_student(self):
        """Test deleting a student"""
        url = reverse(
            "retrieve-update-destroy-students", kwargs={"pk": self.student.id}
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Student.objects.filter(id=self.student.id).exists())

    def test_get_me_student(self):
        """Test retrieving the authenticated user's student profile"""
        response = self.client.get(reverse("getme-students"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.student.id)

    def test_get_me_student_superuser(self):
        """Test retrieving all students when authenticated as a superuser"""
        self.client.force_authenticate(user=self.superuser)
        response = self.client.get(reverse("getme-students"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("email", response.data)
        self.assertEqual(response.data["email"], self.superuser.email)

    def test_unauthorized_access(self):
        """Test that unauthenticated users cannot access student list"""
        self.client.logout()
        response = self.client.get(reverse("create-students"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
