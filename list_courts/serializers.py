from rest_framework import serializers
from .models import ListCourt
from courts.models import Court
from lists.models import List


class ListCourtSerializer(serializers.ModelSerializer):
    court = serializers.PrimaryKeyRelatedField(queryset=Court.objects.all(), many=True)
    lists = serializers.PrimaryKeyRelatedField(queryset=List.objects.all(), many=True)

    class Meta:
        model = ListCourt
        fields = ["id", "court", "lists", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]
