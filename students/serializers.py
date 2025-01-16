import base64

from rest_framework import serializers

from .models import Student


class Base64ImageFieldValidator:
    @staticmethod
    def validate_base_64_image(value):
        try:
            base64.b64decode(value)
        except (ValueError, TypeError):
            raise serializers.ValidationError(
                "The field must contain a valid Base64 encoded string."
            )
        return value


class StudentSerializer(serializers.ModelSerializer):
    profile_img = serializers.CharField(
        required=False,
        allow_blank=True,
        validators=[Base64ImageFieldValidator.validate_base_64_image],
    )

    class Meta:
        model = Student
        fields = [
            "id",
            "birth_date",
            "phone",
            "genre",
            "category",
            "profile_img",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def validate(self, data):
        for key in data.keys():
            if key not in self.fields:
                raise serializers.ValidationError({key: "This field does not exist."})
        return data

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        validated_data["user"] = user
        return super().create(validated_data)
