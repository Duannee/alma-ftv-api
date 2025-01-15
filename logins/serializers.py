from rest_framework import serializers

from users.models import User


class LoginUserSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ["id", "first_name", "email", "password", "is_student"]
        read_only_fields = ["id", "first_name", "is_student"]
