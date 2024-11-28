from django.db import models


class Court(models.Model):
    number = models.IntegerField()
    status = models.CharField(max_length=30)
