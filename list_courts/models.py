from django.db import models
from django.utils.timezone import now

from courts.models import Court
from lists.models import List


class ListCourt(models.Model):
    court = models.ForeignKey(
        Court, on_delete=models.CASCADE, related_name="list_courts"
    )
    lists = models.OneToOneField(
        List, on_delete=models.CASCADE, related_name="list_courts"
    )
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.list.student.name} - Court {self.court.id} - {self.list.class_time}"
        )
