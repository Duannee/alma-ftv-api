from django.db import models
from django.utils.timezone import now


class Coach(models.Model):
    GENRE_CHOICE = [("FEMALE", "FEMALE"), ("MALE", "MALE"), ("OTHERS", "OTHERS")]
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=14)
    genre = models.CharField(max_length=7, choices=GENRE_CHOICE)
    profile_img = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome
