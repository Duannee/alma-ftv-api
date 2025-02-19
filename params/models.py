from django.db import models
from django.utils.timezone import now


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

    def __str__(self):
        return f"{self.class_date} - {self.category} - {self.unit} - {'Active' if self.status else 'Inactive'}"
