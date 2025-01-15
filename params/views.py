from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Params
from .serializers import ParamSerializer


class ParamsListCreateView(ListCreateAPIView):
    queryset = Params.objects.all()
    serializer_class = ParamSerializer


class ParamsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Params.objects.all()
    serializer_class = ParamSerializer
