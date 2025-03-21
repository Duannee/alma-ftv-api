from django.urls import path

from .views import (
    AvailableTimesForTheDayView,
    ListByTimeView,
    ListsCreateView,
    ListsRetrieveUpdateDestroyView,
    StudentsAvailableForAllocationView,
)

urlpatterns = [
    path("create/lists/", ListsCreateView.as_view(), name="create-list"),
    path(
        "update/lists/<int:pk>/",
        ListsRetrieveUpdateDestroyView.as_view(),
        name="retrieve-update-destroy-list",
    ),
    path("list/by-time/", ListByTimeView.as_view(), name="list-by-time"),
    path(
        "students/available-for-allocation/",
        StudentsAvailableForAllocationView.as_view(),
        name="students-available-for-allocation",
    ),
    path(
        "lists/available-times-today/",
        AvailableTimesForTheDayView.as_view(),
        name="lists-available-times-today",
    ),
]
