from rest_framework.generics import CreateAPIView
from .models import Coach
from .serializers import CoachSerializer


class CreateCoachView(CreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
