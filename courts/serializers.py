from rest_framework import serializers

from .models import Court


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]
