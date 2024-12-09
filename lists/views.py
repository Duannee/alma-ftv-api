from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import List
from .serializers import ListSerializer


class ListsListCreateView(ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
