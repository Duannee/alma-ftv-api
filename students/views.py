from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer


class StudentCreateView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroyView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
