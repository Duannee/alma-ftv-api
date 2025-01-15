from django.db import models
from django.utils.timezone import now

from courts.models import Court
from lists.models import List


class ListCourt(models.Model):
    court = models.ManyToManyField(Court, related_name="list_courts")
    lists = models.ManyToManyField(List, related_name="list_courts")
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
