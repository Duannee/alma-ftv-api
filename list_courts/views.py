from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import ListCourt
from .serializers import ListCourtSerializer
from rest_framework.response import Response
from rest_framework import status
from courts.models import Court
from lists.models import List


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

        if not court_id or not student_list_ids:
            return Response(
                {"error": "Court and Students are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not (1 <= int(court_id) <= 8):
            return Response(
                {"error": "Invalid court ID. Must be between 1 and 8."},
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
                list_instance = List.objects.get(id=student_list_id)

                if ListCourt.objects.filter(list=list_instance).exists():
                    continue

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
