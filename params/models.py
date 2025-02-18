from django.db import models
from django.utils.timezone import now
from datetime import time, datetime


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

    class_date = models.DateField()
    status = models.BooleanField(default=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=12, choices=CATEGORY_CHOICE)
    unit = models.CharField(max_length=7, choices=UNIT_CHOICES)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     self.clean()
    #     if self.expires_at not in [self.get_option_1(), self.get_option_2()]:
    #         raise ValueError(
    #             "The `expires_at` field must be either 9:00 PM on the day of creation or 3:30 PM on the day of the class."
    #         )
    #     super().save(*args, **kwargs)

    # def get_option_1(self):
    #     return datetime.combine(now().date(), time(21, 0))

    # def get_option_2(self):
    #     return datetime.combine(self.class_date, time(15, 30))

    def __str__(self):
        return f"{self.class_date} - {self.category} - {self.unit} - {'Active' if self.status else 'Inactive'}"
