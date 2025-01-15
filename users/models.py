from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.crypto import get_random_string


class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        Group, related_name="custom_user_set", blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_permissions", blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = get_random_string(8)
        super().save(*args, **kwargs)
