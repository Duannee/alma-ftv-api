from rest_framework import serializers

from users.models import User


class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_student"]
