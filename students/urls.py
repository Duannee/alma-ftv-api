from django.urls import path
from .views import StudentCreateView

urlpatterns = [
    path("create/students/", StudentCreateView.as_view(), name="students"),
]
