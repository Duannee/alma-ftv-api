from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Params
from .serializers import ParamSerializer


class ListCourtsListCreateView(ListCreateAPIView):
    queryset = Params.objects.all()
    serializer_class = ParamSerializer


class ListCourtsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Params.objects.all()
    serializer_class = ParamSerializer
