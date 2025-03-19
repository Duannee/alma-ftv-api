from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from users.permissions import isStudent

from users.permissions import isSuperUser

from .models import ListParams
from .serializers import ListParamSerializer


class ParamsCreateView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isSuperUser]
    queryset = ListParams.objects.all()
    serializer_class = ListParamSerializer


class ParamsListView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, isStudent]
    queryset = ListParams.objects.all()
    serializer_class = ListParamSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["unit", "category", "class_date"]


class ParamsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ListParams.objects.all()
    serializer_class = ListParamSerializer
