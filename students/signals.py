from django.db.models.signals import post_save
from django.dispatch import receiver

from admissions.models import Admission

from .models import Student


@receiver(post_save, sender=Student)
def create_admission_request(sender, instance, created, **kwargs):
    if created:
        Admission.objects.create(user=instance.user)
