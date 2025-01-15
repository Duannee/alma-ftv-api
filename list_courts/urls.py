from django.urls import path

from .views import (
    ListCourtsListCreateView,
    ListCourtsRetrieveUpdateDestroyView,
)

urls_patterns = [
    path(
        "create/lists/courts/",
        ListCourtsListCreateView.as_view(),
        name="list-create-list-courts",
    ),
    path(
        "update/list/courts/<int:pk>",
        ListCourtsRetrieveUpdateDestroyView.as_view(),
        name="retrieve-update-destroy-list-courts",
    ),
]
