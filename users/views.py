from rest_framework.generics import CreateAPIView, UpdateAPIView

from .models import User
from .serializers import UserSerializer


class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
