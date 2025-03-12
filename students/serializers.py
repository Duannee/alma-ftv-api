import base64

from rest_framework import serializers

from users.models import User

from .models import Student


class UserStudentSerializer(serializers.ModelSerializer):

    isPendingStudent = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "is_superuser",
            "isPendingStudent",
        ]

    def get_isPendingStudent(self, obj):
        return Student.objects.filter(user=obj).exists() and not obj.is_student


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

    user = UserStudentSerializer(read_only=True)

    class Meta:
        model = Student
        fields = [
            "user",
            "id",
            "birth_date",
            "phone",
            "genre",
            "category",
            "unit",
            "profile_img",
            "created_at",
            "updated_at",
            "playing_side",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def validate(self, data):
        request = self.context.get("request")
        user = request.user

        if self.instance is None and Student.objects.filter(user=user).exists():
            raise serializers.ValidationError(
                {"error": "Student profile already exists"}
            )

        for key in data.keys():
            if key not in self.fields:
                raise serializers.ValidationError({key: "This field does not exist."})

        return data

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        validated_data["user"] = user
        return super().create(validated_data)
