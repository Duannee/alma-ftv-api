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
from users.permissions import isSuperUser
from rest_framework_simplejwt.authentication import JWTAuthentication


from .models import ListCourt
from .serializers import ListCourtSerializer


class ListCourtsListCreateView(ListCreateAPIView):
    queryset = ListCourt.objects.all()
    serializer_class = ListCourtSerializer


class ListCourtsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ListCourt.objects.all()
    serializer_class = ListCourtSerializer


class AllocateStudentsCourtsView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isSuperUser]

    def post(self, request, *args, **kwargs):
        student_list_ids = request.data.get("student_list_ids", [])
        court_number = request.data.get("court_number")

        if not student_list_ids or not court_number:
            return Response(
                {"error": "Student list IDs and court number are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            court = Court.objects.get(number=court_number, status="ACTIVE")
        except Court.DoesNotExist:
            return Response(
                {"error": f"Court {court_number} not found or inactive"},
                status=status.HTTP_404_NOT_FOUND,
            )

        allocated_students = []
        errors = []
        for student_list_id in student_list_ids:
            try:
                list_instance = List.objects.get(id=student_list_id)

                if ListCourt.objects.filter(list=list_instance).exists():
                    errors.append(
                        f"Student {list_instance.student.name} is already allocated to a court"
                    )

                    continue

                ListCourt.objects.create(court=court, list=list_instance)
                allocated_students.append(list_instance.student.name)
            except List.DoesNotExist:
                errors.append(f"List entry with ID {student_list_id} not found")
        if errors:
            return Response(
                {
                    "message": f"Students {allocated_students} successfully allocated to Court {court.number}",
                    "errors": errors,
                },
                status=status.HTTP_207_MULTI_STATUS,
            )
        return Response(
            {
                "message": f"Students {allocated_students} successfully allocated to Court {court.number}"
            },
            status=status.HTTP_200_OK,
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
