from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from .serializers import LoginUserSerializer

# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt


# @method_decorator(csrf_exempt, name="dispatch")
class LoginView(CreateAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            raise AuthenticationFailed("Email and password are required")

        user = authenticate(request, username=email, password=password)
        if not user:
            raise AuthenticationFailed("Invalid credentials")

        refresh = RefreshToken.for_user(user)

        user_data = LoginUserSerializer(user).data

        return Response(
            {
                **user_data,
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            }
        )
