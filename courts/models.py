from django.db import models
from django.utils.timezone import now


class Court(models.Model):
    number = models.IntegerField()
    status = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
