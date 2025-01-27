from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import List
from .utils import can_add_to_list


class ListSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=List.objects.values_list("student", flat=True)
    )

    class Meta:
        model = List
        fields = ["id", "student", "list_params", "class_time"]
        read_only_fields = ["created_at", "updated_at"]

    def validate(self, data):
        student = data["student"]

        if not can_add_to_list(student):
            raise ValidationError(
                "You have already reached the frequency limit this week."
            )

        return data
