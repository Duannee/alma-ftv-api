from rest_framework import serializers

from .models import StudentPlans


class StudentPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPlans
        fields = [
            "id",
            "student",
            "payment_day",
            "weekly_frequency",
            "type_plan",
            "value",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]
