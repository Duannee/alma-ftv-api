from django.forms import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from .models import Payment
from .serializers import PaymentSerializer
from students.models import Student


class CreatePaymentView(CreateAPIView):
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        student_payment = get_object_or_404(Student, pk=self.kwargs.get("student_id"))

        if Payment.objects.filter(student=student_payment).exists():
            raise ValidationError(
                {"error": "Already exists a payment for this student"}
            )
        return serializer.save(student=student_payment)
