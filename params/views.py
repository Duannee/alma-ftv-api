from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import ListParams
from .serializers import ListParamSerializer


class ParamsListCreateView(ListCreateAPIView):
    queryset = ListParams.objects.all()
    serializer_class = ListParamSerializer


class ParamsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ListParams.objects.all()
    serializer_class = ListParamSerializer
