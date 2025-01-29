from django.urls import path

from .views import (
    ListsListCreateView,
    ListsRetrieveUpdateDestroyView,
    ListByTimeView,
    StudentsAvailableForCourtsView,
)

urlpatterns = [
    path("create/lists/", ListsListCreateView.as_view(), name="list-create-list"),
    path(
        "update/lists/<int:pk>/",
        ListsRetrieveUpdateDestroyView.as_view(),
        name="retrieve-update-destroy-list",
    ),
    path("list/by-time/", ListByTimeView.as_view(), name="list-by-time"),
    path(
        "students/available/",
        StudentsAvailableForCourtsView.as_view(),
        name="students-available",
    ),
]
