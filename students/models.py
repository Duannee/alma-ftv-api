from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):
    CATEGORY_CHOICE = [
        ("BEGINNER", "BEGINNER"),
        ("INTERMEDIARY", "INTERMEDIARY"),
        ("ADVANCED", "ADVANCED"),
    ]
    name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)])
    email = models.EmailField()
    phone = models.TextField(max_length=20)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE)

    def __str__(self) -> str:
        return self.nome
