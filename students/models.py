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
    PLAYING_SIDE_CHOICES = [
        ("RIGHT", "RIGHT"),
        ("LEFT", "LEFT"),
    ]
    UNIT_CHOICES = [
        ("IPANEMA", "IPANEMA"),
        ("BARRA", "BARRA"),
    ]

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="students"
    )
    unit = models.CharField(max_length=7, choices=UNIT_CHOICES)
    birth_date = models.DateField()
    phone = models.CharField(max_length=20)
    genre = models.CharField(max_length=7, choices=GENRE_CHOICE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE)
    profile_img = models.TextField(blank=True)
    frequency_of_classes = models.CharField(
        max_length=2, choices=FREQUENCY_OF_CLASSES_CHOICES
    )
    playing_side = models.CharField(max_length=5, choices=PLAYING_SIDE_CHOICES)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
