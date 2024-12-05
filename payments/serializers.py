from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ["id", "student", "pay_day", "value", "status"]
        depth = 1
        read_only_fields = ["student", "created_at", "updated_at"]

    def validate(self, data):
        for key in data.keys():
            if key not in self.fields:
                raise serializers.ValidationError({key: "This field does not exist."})
        return data
