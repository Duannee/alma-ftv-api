from django.utils.timezone import now, timedelta
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response

from courts.models import Court
from lists.models import List

from .models import ListCourt
from .serializers import ListCourtSerializer


class ListCourtsListCreateView(ListCreateAPIView):
    queryset = ListCourt.objects.all()
    serializer_class = ListCourtSerializer


class ListCourtsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ListCourt.objects.all()
    serializer_class = ListCourtSerializer


class AllocateStudentsCourtsView(CreateAPIView):
    queryset = ListCourt.objects.all()
    serializer_class = ListCourtSerializer

    def create(self, request, *args, **kwargs):
        court_id = request.data.get("court_id")
        student_list_ids = request.data.get("student_list_ids")
        class_time = request.data.get("class_time")

        if not court_id or not student_list_ids or not class_time:
            return Response(
                {"error": "Court, Students and Class Time are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            court = Court.objects.get(id=court_id)
        except Court.DoesNotExist:
            return Response(
                {"error": "Court not found"}, status=status.HTTP_404_NOT_FOUND
            )

        for student_list_id in student_list_ids:
            try:
                list_instance = List.objects.get(
                    id=student_list_id, class_time=class_time
                )

                existing_allocation = (
                    ListCourt.objects.filter(list=list_instance)
                    .select_related("court")
                    .first()
                )

                if existing_allocation:
                    existing_allocation.court = court
                    existing_allocation.save()
                else:
                    ListCourt.objects.create(list=list_instance, court=court)

            except List.DoesNotExist:
                return Response(
                    {"error": f"List entry with ID {student_list_id} not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

        return Response(
            {"message": "Students successfully allocated to the courts"},
            status=status.HTTP_201_CREATED,
        )


class ClearPreviousDayAllocationsView(DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        yesterday = now().date() - timedelta(days=1)

        delete_count, _ = ListCourt.objects.filter(created_at__date=yesterday).delete()

        if delete_count == 0:
            return Response(
                {"message": "No allocations to delete from yesterday"},
                status=status.HTTP_200_OK,
            )

        return Response(
            {"message": f"{delete_count} allocations deleted"},
            status=status.HTTP_200_OK,
        )


class MyCourtView(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        user = request.user

        if not user.is_authenticated:
            return Response(
                {"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED
            )

        my_allocation = (
            ListCourt.objects.filter(list__student=user).select_related("court").first()
        )

        if not my_allocation:
            return Response(
                {"message": "You are not allocated to any court"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {
                "court_id": my_allocation.court.id,
                "court_number": my_allocation.court.number,
                "class_time": my_allocation.lists.class_time,
            },
            status=status.HTTP_200_OK,
        )
