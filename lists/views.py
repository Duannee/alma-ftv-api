from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from list_courts.models import ListCourt

from .models import List
from .serializers import ListSerializer


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
    filterset_fields = ["class_time", "list_params__category"]

    def get_queryset(self):
        queryset = super().get_queryset()

        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.filter(list_params__category=user.category)

        return queryset


class StudentsAvailableForCourtsView(ListAPIView):
    serializer_class = ListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["class_time"]

    def get_queryset(self):
        class_time = self.request.query_params.get("class_time")

        user = self.request.user
        if not user.is_authenticated:
            return List.objects.none()

        student_category = user.category

        students_in_list = List.objects.filter(
            class_time=class_time, student__category=student_category
        )

        students_in_court = ListCourt.objects.values_list("list_id", flat=True)

        return students_in_list.exclude(id__in=students_in_court)
