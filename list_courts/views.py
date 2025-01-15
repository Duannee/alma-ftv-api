from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import ListCourt
from .serializers import ListCourtSerializer


class ListCourtsListCreateView(ListCreateAPIView):
    queryset = ListCourt.objects.all()
    serializer_class = ListCourtSerializer


class ListCourtsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ListCourt.objects.all()
    serializer_class = ListCourtSerializer
