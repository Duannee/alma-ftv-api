from django.urls import path

from .views import ListCreateAPIView, ListRetrieveUpdateDestroyView

urls_patterns = [
    path(
        "create/lists/", ListCreateAPIView.as_view(), name="list-create-list"
    ),
    path(
        "update/lists/<int:pk>/",
        ListRetrieveUpdateDestroyView.as_view(),
        name="retrieve-update-destroy-list",
    ),
]
