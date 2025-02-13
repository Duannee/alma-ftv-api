from django.db import models
from django.utils.timezone import now
from datetime import time


class ListParams(models.Model):
    CATEGORY_CHOICE = [
        ("BEGINNER", "BEGINNER"),
        ("INTERMEDIARY", "INTERMEDIARY"),
        ("ADVANCED", "ADVANCED"),
        ("WARNING", "WARNING"),
        ("WEEKEND", "WEEKEND"),
    ]

    UNIT_CHOICES = [
        ("IPANEMA", "IPANEMA"),
        ("BARRA", "BARRA"),
    ]

    CLASS_TIME_CHOICES = [
        (time(6, 0), "06:00"),
        (time(7, 0), "07:00"),
        (time(8, 0), "08:00"),
        (time(9, 0), "09:00"),
        (time(17, 0), "17:00"),
        (time(18, 0), "18:00"),
        (time(6, 15), "06:15"),
        (time(7, 15), "07:15"),
        (time(8, 15), "08:15"),
    ]

    class_date = models.DateField()
    class_time = models.TimeField(choices=CLASS_TIME_CHOICES)
    status = models.BooleanField(default=True)
    expires_at = models.DateTimeField()
    description = models.TextField()
    category = models.CharField(max_length=12, choices=CATEGORY_CHOICE)
    unit = models.CharField(max_length=7, choices=UNIT_CHOICES)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.class_date} - {self.category} - {"Active" if self.status else "Inactive"}"
