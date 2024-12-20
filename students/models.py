from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Student(models.Model):
    CATEGORY_CHOICE = [
        ("BEGINNER", "BEGINNER"),
        ("INTERMEDIARY", "INTERMEDIARY"),
        ("ADVANCED", "ADVANCED"),
    ]
    GENRE_CHOICE = [("FEMALE", "FEMALE"), ("MALE", "MALE"), ("OTHERS", "OTHERS")]

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="students")
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    genre = models.CharField(max_length=7, choices=GENRE_CHOICE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE)
    profile_img = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
