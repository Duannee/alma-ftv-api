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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["class_time"]

    def get_queryset(self):
        queryset = super().get_queryset()

        class_time = self.request.query_params.get("class_time")

        if class_time:
            queryset = queryset.filter(class_time=class_time)

        return queryset


class ListsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
