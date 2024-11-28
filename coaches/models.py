from django.db import models


class Coach(models.Model):
    GENRE_CHOICE = [("FEMALE", "FEMALE"), ("MALE", "MALE"), ("OTHERS", "OTHERS")]
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.TextField(max_length=20)
    genre = models.CharField(max_length=7, choices=GENRE_CHOICE)
    profile_img = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nome
