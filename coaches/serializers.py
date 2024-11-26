from rest_framework import serializers
from .models import Coach


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = "__all__"

    def validate(self, data):
        for key in data.keys():
            if key not in self.fields:
                raise serializers.ValidationError({key: "This field does not exist."})
        return data

    def validate(self, attrs):
        name = attrs.get("name")
        email = attrs.get("email")

        if Coach.objects.filter(name=name).exists():
            raise serializers.ValidationError(
                "There is already a coach with that name , please choose another one"
            )

        if Coach.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                "There is already a coach with that email, please choose another one"
            )

        return attrs
