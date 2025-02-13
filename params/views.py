from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView,
)


from .models import ListParams
from .serializers import ListParamSerializer


class ParamsCreateView(CreateAPIView):
    queryset = ListParams.objects.all()
    serializer_class = ListParamSerializer


class ParamsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ListParams.objects.all()
    serializer_class = ListParamSerializer
