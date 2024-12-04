from django.db import models
from django.utils.timezone import now


class List(models.Model):
    CATEGORY_CHOICE = [
        ("BEGINNER", "BEGINNER"),
        ("INTERMEDIARY", "INTERMEDIARY"),
        ("ADVANCED", "ADVANCED"),
    ]
    CLASS_TIME_CHOICES = [
        ("06:00", "06:00"),
        ("07:00", "07:00"),
        ("08:00", "08:00"),
        ("09:00", "09:00"),
        ("17:00", "17:00"),
        ("18:00", "18:00"),
        ("06:15", "06:15"),
        ("07:15", "07:15"),
        ("08:15", "08:15"),
    ]
    date_day = models.DateField(auto_now_add=True)
    student = models.ForeignKey(
        "students.student", on_delete=models.CASCADE, related_name="lists"
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE)
    class_time = models.CharField(max_length=5, choices=CLASS_TIME_CHOICES)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.name} - {self.date_day} - {self.class_time}"
