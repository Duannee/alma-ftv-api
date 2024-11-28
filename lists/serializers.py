from rest_framework import serializers
from .models import List


class ListSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()

    class Meta:
        model = List
        fields = ["id", "date_day", "student_id", "category"]

        def validate(self, data):
            student = data.get("student_id")
            category = data.get("category")

            if student.category != category:
                raise serializers.ValidationError(
                    "The student's category does not match the list category."
                )

            return data
