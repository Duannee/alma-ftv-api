from rest_framework import serializers

from .models import ListParams


class ListParamSerializer(serializers.ModelSerializer):

    class_time = serializers.TimeField(format="%H:%M")

    class Meta:
        model = ListParams
        fields = [
            "id",
            "class_date",
            "class_time",
            "status",
            "expires_at",
            "description",
            "category",
            "unit",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]
