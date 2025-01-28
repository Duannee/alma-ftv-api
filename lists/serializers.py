from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.timezone import localtime

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

        now = localtime()
        created_at = self.instance.created_at if self.instance else now
        deadline = created_at.replace(hour=21, minute=0, second=0, microsecond=0)

        if now > deadline:
            raise ValidationError(
                "You cannot add to the list after 21:00 of the same day."
            )

        return data
