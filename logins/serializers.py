from rest_framework import serializers
from users.models import User


class LoginUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ["id", "name", "email", "password"]
        read_only_fields = ["id", "name"]
