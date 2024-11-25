from django.db import models


class Student(models.Model):
    CATEGORY_CHOICE = [
        ("BEGINNER", "BEGINNER"),
        ("INTERMEDIARY", "INTERMEDIARY"),
        ("ADVANCED", "ADVANCED"),
    ]
    GENRE_CHOICE = [("FEMALE", "FEMALE"), ("MALE", "MALE"), ("OTHERS", "OTHERS")]

    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    genre = models.CharField(max_length=7, choices=GENRE_CHOICE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE)

    def __str__(self) -> str:
        return self.name
