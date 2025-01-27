from django.db import models
from django.utils.timezone import now


class ListParams(models.Model):
    CATEGORY_CHOICE = [
        ("BEGINNER", "BEGINNER"),
        ("INTERMEDIARY", "INTERMEDIARY"),
        ("ADVANCED", "ADVANCED"),
    ]
    class_date = models.DateField()
    status = models.BooleanField(default=True)
    expires_at = models.DateTimeField()
    description = models.TextField()
    category = models.CharField(max_length=12, choices=CATEGORY_CHOICE)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
