from rest_framework import serializers

from courts.models import Court
from lists.models import List

from .models import ListCourt


class ListCourtSerializer(serializers.ModelSerializer):
    court = serializers.PrimaryKeyRelatedField(
        queryset=Court.objects.all(),
    )
    lists = serializers.PrimaryKeyRelatedField(
        queryset=List.objects.all(),
    )

    class Meta:
        model = ListCourt
        fields = ["id", "court", "lists", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]
