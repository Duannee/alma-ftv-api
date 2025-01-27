from rest_framework import status
from rest_framework.generics import DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.models import User
from users.permissions import isSuperUser

from .serializers import AdmissionSerializer


class AdmissionListView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isSuperUser]
    queryset = User.objects.filter(is_student=False)
    serializer_class = AdmissionSerializer


class ApproveAdmissionView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isSuperUser]
    queryset = User.objects.filter(is_student=False)
    serializer_class = AdmissionSerializer

    def update(self, request, *args, **kwargs):
        user = self.get_object()

        user.is_student = True
        user.save()
        return Response({"message": "Approved user!"}, status=status.HTTP_200_OK)


class RejectAdmissionView(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isSuperUser]
    queryset = User.objects.filter(is_student=False)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(
            {"message": "Application for admission rejected"},
            status=status.HTTP_204_NO_CONTENT,
        )
