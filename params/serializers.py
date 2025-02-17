from rest_framework import serializers

from .models import ListParams


class ListParamSerializer(serializers.ModelSerializer):

    class_time = serializers.TimeField(format="%H:%M", required=False, allow_null=True)
    expires_at = serializers.ChoiceField(
        choices=[
            ("option_1", "9:00 pm on the day of creation"),
            ("option_2", "3:30 pm on the day of the class"),
        ]
    )

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
        read_only_fields = ["created_at", "updated_at", "expires_at"]

    def validate_expires_at(self, value):
        instance = self.instance or ListParams()

        if value == "option_1":
            return instance.get_option_1()
        elif value == "option_2":
            return instance.get_option_2()
        raise serializers.ValidationError(
            "The `expires_at` field must be 'option_1' or 'option_2'."
        )
