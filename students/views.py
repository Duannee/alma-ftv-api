from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Student
from .serializers import StudentSerializer, UserStudentSerializer

from rest_framework.response import Response


class StudentListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)


class StudentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GetMeStudentView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return [user]

        if user.is_student:
            student = Student.objects.filter(user=user).first()
            if student:
                return [student]

        return []

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if self.request.user.is_superuser:
            serializer = UserStudentSerializer(queryset, many=True)
        else:
            serializer = StudentSerializer(queryset, many=True)

        return Response(serializer.data, status=200)
