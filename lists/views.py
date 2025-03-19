from django.utils.timezone import now
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from list_courts.models import ListCourt
from users.permissions import isSuperUser

from .models import List
from .serializers import ListSerializer
from .category_unit_time import CATEGORY_TIMES_BY_UNIT
from datetime import datetime
from students.models import Student


class ListsCreateView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

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


class StudentsAvailableForAllocationView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isSuperUser]

    def get_queryset(self):
        category = self.request.query_params.get("category")
        unit = self.request.query_params.get("unit")
        class_time = self.request.query_params.get("class_time")

        if not category or not unit or not class_time:
            return List.objects.none()

        return List.objects.filter(
            list_params__category=category,
            list_params__unit=unit,
            class_time=class_time,
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset.exists():
            return Response(
                {
                    "error": "No students found for the given category, unit, and class time"
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AvailableTimesForTheDayView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        try:
            student = Student.objects.get(user=user)
        except Student.DoesNotExist:
            return Response(
                {"error": "Student profile not found"}, status=status.HTTP_404_NOT_FOUND
            )

        today_weekday = datetime.now().weekday()

        student_category = student.category
        student_unit = student.unit

        available_times = (
            CATEGORY_TIMES_BY_UNIT.get(student_category, {})
            .get(student_unit, {})
            .get(today_weekday, [])
        )

        formatted_times = [t.strftime("%H:%M") for t in available_times]

        return Response({"available_times": formatted_times}, status=status.HTTP_200_OK)


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
