from django.db import models
from django.utils.timezone import now

from students.models import Student


class StudentPlans(models.Model):
    FREQUENCY_CHOICES = [
        ("1X", "1X"),
        ("2X", "2X"),
        ("3X", "3X"),
        ("4X", "4X"),
        ("5X", "5X"),
    ]
    PLAN_CHOICES = [("QUARTERLY", "QUARTERLY"), ("SEMIANNUAL", "SEMIANNUAL")]
    STATUS_CHOICES = [("ACTIVE", "ACTIVE"), ("INACTIVE", "INACTIVE")]
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="student_plans"
    )
    payment_day = models.IntegerField()
    weekly_frequency = models.CharField(
        max_length=2, choices=FREQUENCY_CHOICES
    )
    type_plan = models.CharField(max_length=10, choices=PLAN_CHOICES)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
