from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import localtime, now


class List(models.Model):
    student = models.ForeignKey(
        "students.Student", on_delete=models.CASCADE, related_name="lists"
    )
    list_params = models.ForeignKey(
        "params.ListParams", on_delete=models.CASCADE, related_name="lists"
    )
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        now = localtime()
        deadline = self.created_at.replace(hour=21, minute=0, second=0, microsecond=0)

        if now > deadline:
            raise ValidationError(
                "You cannot add to the list after 21:00 of the same day."
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name}  - {self.class_time}"
