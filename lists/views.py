from django.utils.timezone import now
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from rest_framework.response import Response

from list_courts.models import ListCourt

from .models import List
from .serializers import ListSerializer


class ListsCreateView(CreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            self.perform_create(serializer)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(serializer.data, status=status.HTTP_201_CREATED)


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


class AvailableTimesForTheDayView(ListAPIView):
    def get_queryset(self):
        today = now().date()
        return (
            List.objects.filter(created_at__date=today)
            .values_list("class_time", flat=True)
            .distinct()
        )

    def list(self, request, *args, **kwargs):

        return Response(
            {"available_times": list(self.get_queryset())}, status=status.HTTP_200_OK
        )


class AvailableTimesForCategoryView(ListAPIView):
    def list(self, request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            return Response(
                {"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED
            )

        user_category = user.category

        available_times = (
            List.objects.filter(list_params__category=user_category)
            .values_list("class_time", flat=True)
            .distinct()
        )
        return Response(
            {"available_times": list(available_times)}, status=status.HTTP_200_OK
        )
