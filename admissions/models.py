from django.db import models


class Admission(models.Model):
    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="admissions"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Admission Request - {self.user.username}"
