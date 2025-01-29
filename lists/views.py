from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import List
from .serializers import ListSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ListsListCreateView(ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListByTimeView(ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["class_time"]
