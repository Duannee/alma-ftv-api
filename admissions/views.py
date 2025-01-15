from rest_framework.generics import UpdateAPIView, DestroyAPIView
from .models import Admission
from .serializers import AdmissionSerializer


class AdmissionUpdateView(UpdateAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer


class AdmissionDeleteView(DestroyAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
