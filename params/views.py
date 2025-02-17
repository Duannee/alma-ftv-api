from datetime import timedelta
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now
from rest_framework.response import Response


from .models import ListParams
from .serializers import ListParamSerializer


class ParamsCreateView(CreateAPIView):
    queryset = ListParams.objects.all()
    serializer_class = ListParamSerializer


class ParamsListView(ListAPIView):
    queryset = ListParams.objects.all()
    serializer_class = ListParamSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["unit", "category", "class_date"]


class ParamsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ListParams.objects.all()
    serializer_class = ListParamSerializer


class AvailableClassTimeParamsView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        today = now().date()
        tomorrow = now().date() + timedelta(days=1)

        user_category = user.category
        user_unit = user.unit

        weekday = tomorrow.weekday()
        valid_times = (
            ListParams.CATEGORY_TIMES_BY_UNIT.get(user_category, {})
            .get(user_unit, {})
            .get(weekday, [])
        )

        return valid_times

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        formatted_times = [time.strftime("%H:%M") for time in queryset]

        return Response({"available_times": formatted_times})
