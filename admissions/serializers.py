from rest_framework import serializers

from .models import AdmissionModel


class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionModel
        fields = "__all__"
