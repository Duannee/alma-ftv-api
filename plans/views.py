from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import StudentPlans
from .serializers import StudentPlanSerializer


class ListCourtsListCreateView(ListCreateAPIView):
    queryset = StudentPlans.objects.all()
    serializer_class = StudentPlanSerializer


class ListCourtsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = StudentPlans.objects.all()
    serializer_class = StudentPlanSerializer
