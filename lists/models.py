from django.db import models
from django.utils.timezone import now


class List(models.Model):
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
    student = models.ForeignKey(
        "students.Student", on_delete=models.CASCADE, related_name="lists"
    )
    list_params = models.ForeignKey(
        "params.ListParams", on_delete=models.CASCADE, related_name="lists"
    )
    class_time = models.CharField(max_length=5, choices=CLASS_TIME_CHOICES)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.id}  - {self.class_time}"
