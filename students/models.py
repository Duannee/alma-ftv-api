from django.db import models
from django.utils.timezone import now


class Student(models.Model):
    CATEGORY_CHOICE = [
        ("BEGINNER", "BEGINNER"),
        ("INTERMEDIARY", "INTERMEDIARY"),
        ("ADVANCED", "ADVANCED"),
    ]
    GENRE_CHOICE = [
        ("FEMALE", "FEMALE"),
        ("MALE", "MALE"),
        ("OTHERS", "OTHERS"),
    ]
    FREQUENCY_OF_CLASSES_CHOICES = [
        ("1X", "1X"),
        ("2X", "2X"),
        ("3X", "3X"),
        ("4X", "4X"),
        ("5X", "5X"),
    ]

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="students"
    )
    birth_date = models.DateField()
    phone = models.CharField(max_length=20)
    genre = models.CharField(max_length=7, choices=GENRE_CHOICE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE)
    profile_img = models.TextField(null=True, blank=True)
    frequency_of_classes = models.CharField(
        max_length=2, choices=FREQUENCY_OF_CLASSES_CHOICES
    )
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
