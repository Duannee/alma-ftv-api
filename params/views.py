from datetime import timedelta
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from .models import ListParams
from .serializers import ListParamSerializer


class ParamsCreateView(CreateAPIView):
    queryset = ListParams.objects.all()
    serializer_class = ListParamSerializer


class ParamsListView(ListAPIView):
    queryset = ListParams.objects.all()
    serializer_class = ListParamSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["unit", "category", "class_date"]


class ParamsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ListParams.objects.all()
    serializer_class = ListParamSerializer
