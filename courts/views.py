from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Court
from .serializers import CourtSerializer


class CourtListCreateView(ListCreateAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer


class CourtRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer


class CourtsByTimeView(ListAPIView):
    serializer_class = CourtSerializer

    def get_queryset(self):
        return Court.objects.all()
