from django.db import models


class AdmissionModel(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="admissions"
    )
