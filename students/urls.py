from django.urls import path
from .views import StudentListCreateView

urlpatterns = [
    path(
        "create/students/", StudentListCreateView.as_view(), name="list-create-students"
    ),
]
