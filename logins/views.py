from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomTokenObtainPairSerializer


class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            raise AuthenticationFailed("Email and password are required")

        user = authenticate(request, username=email, password=password)
        if not user:
            raise AuthenticationFailed("Invalid credentials")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.validated_data

        return Response(
            {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "is_student": user.is_student,
                "access_token": tokens["access"],
                "refresh_token": tokens["refresh"],
            }
        )
