from django.db import models
from students.models import Student


class Payment(models.Model):
    STATUS_PAYMENT_CHOICES = [
        ("UP_TO_DATE", "UP_TO_DATE"),
        ("PENDING", "PENDING"),
        ("LATE", "LATE"),
    ]
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    pay_day = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=STATUS_PAYMENT_CHOICES, default="UP_TO_DATE"
    )


def __str__(self) -> str:
    return f"{self.student_id.name} - {self.pay_day}"
