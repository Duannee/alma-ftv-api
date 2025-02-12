from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Student
from .serializers import StudentSerializer, UserStudentSerializer


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

        return [user]

    def list(self, request, *args, **kwargs):
        user = self.request.user
        student = Student.objects.filter(user=user).first()

        if user.is_superuser:
            serializer = UserStudentSerializer(user)
            return Response(serializer.data, status=200)

        if user.is_student and student:
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=200)

        if student and not user.is_student:
            serializer = UserStudentSerializer(user)
            data = serializer.data
            data["isPendingStudent"] = True
            return Response(data, status=200)

        serializer = UserStudentSerializer(user)
        return Response(serializer.data, status=200)
