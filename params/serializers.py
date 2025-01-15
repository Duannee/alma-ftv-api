from rest_framework import serializers

from .models import Params


class ParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Params
        fields = [
            "id",
            "class_date",
            "status",
            "expires_at",
            "description",
            "category",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]
