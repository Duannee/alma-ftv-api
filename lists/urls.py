from django.urls import path

from .views import (
    AvailableTimesForTheDayView,
    ListByTimeView,
    ListsListCreateView,
    ListsRetrieveUpdateDestroyView,
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
        "students/available-for-courts/",
        StudentsAvailableForCourtsView.as_view(),
        name="students-available",
    ),
    path(
        "lists/available-times-today/",
        AvailableTimesForTheDayView.as_view(),
        name="lists-available-times-today",
    ),
]
