from django.db import models
from students.models import Student
from django.utils.timezone import now


class Payment(models.Model):
    STATUS_PAYMENT_CHOICES = [
        ("UP_TO_DATE", "UP_TO_DATE"),
        ("PENDING", "PENDING"),
        ("LATE", "LATE"),
    ]
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="payments"
    )
    payment_date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=STATUS_PAYMENT_CHOICES, default="UP_TO_DATE"
    )
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self) -> str:
    return f"{self.student_id.name} - {self.pay_day}"
