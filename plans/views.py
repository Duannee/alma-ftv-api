from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import StudentPlans
from .serializers import StudentPlanSerializer


class StudentPlanListCreateView(ListCreateAPIView):
    queryset = StudentPlans.objects.all()
    serializer_class = StudentPlanSerializer


class StudentPlanRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = StudentPlans.objects.all()
    serializer_class = StudentPlanSerializer
