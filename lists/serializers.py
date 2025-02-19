from django.utils.timezone import localtime
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from students.models import Student

from .models import List
from .utils import can_add_to_list


class ListSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    student_name = serializers.SerializerMethodField()
    category_name = serializers.CharField(
        source="list_params.category.name", read_only=True
    )
    class_time = serializers.TimeField(format="%H:%M")

    class Meta:
        model = List
        fields = [
            "id",
            "student",
            "class_time",
            "student_name",
            "list_params",
            "category_name",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def get_student_name(self, obj):
        return f"{obj.student.user.first_name} {obj.student.user.last_name}".strip()

    def validate(self, data):
        try:
            student = data["student"]
            list_params = data["list_params"]

            if student.category != list_params.category:
                raise ValidationError(
                    "You can only subscribe to lists in your own category."
                )

            now = localtime()
            created_at = (
                self.instance.created_at if self.instance and self.instance.pk else now
            )
            deadline = created_at.replace(hour=21, minute=0, second=0, microsecond=0)

            if now > deadline:
                raise ValidationError(
                    "You cannot add to the list after 21:00 of the same day."
                )

        except Exception as e:
            raise serializers.ValidationError({"error": str(e)})

        return data
