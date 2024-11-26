from rest_framework.generics import CreateAPIView
from .models import Student
from .serializers import StudentSerializer


class UserRegisterView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
