from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView
from users.models import User
from .serializers import AdmissionSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status


class AdmissionListView(ListAPIView):
    queryset = User.objects.filter(is_student=False)
    serializer_class = AdmissionSerializer
    permission_classes = [IsAdminUser]


class ApproveAdmissionView(UpdateAPIView):
    queryset = User.objects.filter(is_student=False)
    serializer_class = AdmissionSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_student = True
        user.save()
        return Response({"message": "Approved user!"}, status=status.HTTP_200_OK)
