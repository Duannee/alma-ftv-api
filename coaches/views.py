from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Coach
from .serializers import CoachSerializer


class CoachListCreateView(ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class CoachRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
