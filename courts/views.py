from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Court
from .serializers import CourtSerializer


class CourtView(ListCreateAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer


class CourtView(RetrieveUpdateDestroyAPIView):
    queryset = Court.objects.all()
    serializer_class = CourtSerializer
