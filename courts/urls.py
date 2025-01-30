from django.urls import path

from .views import (
    CourtListCreateView,
    CourtRetrieveUpdateDestroyView,
    CourtsByTimeView,
)

urls_patterns = [
    path(
        "create/courts/",
        CourtListCreateView.as_view(),
        name="list-create-courts",
    ),
    path(
        "update/courts/<int:pk>/",
        CourtRetrieveUpdateDestroyView.as_view(),
        name="retrieve-update-destroy-courts",
    ),
    path("courts/all/", CourtsByTimeView.as_view(), name="courts-all"),
]
