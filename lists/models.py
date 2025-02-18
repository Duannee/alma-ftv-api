from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import localtime, now
from datetime import time


class List(models.Model):

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
    student = models.ForeignKey(
        "students.Student", on_delete=models.CASCADE, related_name="lists"
    )
    list_params = models.ForeignKey(
        "params.ListParams", on_delete=models.CASCADE, related_name="lists"
    )
    class_time = models.TimeField(choices=CLASS_TIME_CHOICES)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        now = localtime()
        created_at = self.created_at if self.pk else now
        deadline = created_at.replace(hour=21, minute=0, second=0, microsecond=0)

        if now > deadline:
            raise ValidationError(
                "You cannot add to the list after 21:00 of the same day."
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.id} - {self.class_time}"
