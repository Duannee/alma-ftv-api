from rest_framework import serializers

from .models import ListParams


class ListParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListParams
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
