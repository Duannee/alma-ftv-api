from django.db import models
from django.utils.timezone import now


class Court(models.Model):
    STATUS_CHOICE = [("ACTIVE", "ACTIVE"), ("INACTIVE", "INACTIVE")]
    number = models.IntegerField(unique=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICE, default="ACTIVE")
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.number} - {self.status} "
