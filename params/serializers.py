from rest_framework import serializers

from .models import ListParams


class ListParamSerializer(serializers.ModelSerializer):

    expires_at = serializers.DateTimeField(required=False, allow_null=True)

    class Meta:
        model = ListParams
        fields = [
            "id",
            "class_date",
            "status",
            "expires_at",
            "description",
            "category",
            "unit",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at", "expires_at"]
