from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView
from users.models import User
from .serializers import AdmissionSerializer
from rest_framework.permissions import IsAdminUser


class AdmissionListView(ListAPIView):
    queryset = User.objects.filter(is_student=False)
    serializer_class = AdmissionSerializer
    permission_classes = [IsAdminUser]
