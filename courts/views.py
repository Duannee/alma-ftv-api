from rest_framework.generics import (
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
