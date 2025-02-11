from django.urls import path

from .views import (
    GetMeStudentView,
    StudentListCreateView,
    StudentRetrieveUpdateDestroyView,
)

urlpatterns = [
    path(
        "create/students/",
        StudentListCreateView.as_view(),
        name="create-students",
    ),
    path(
        "update/students/<int:pk>/",
        StudentRetrieveUpdateDestroyView.as_view(),
        name="retrieve-update-destroy-students",
    ),
    path(
        "getme/student/",
        GetMeStudentView.as_view(),
        name="getme-students",
    ),
]
