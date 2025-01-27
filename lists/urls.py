from django.urls import path

from .views import ListsListCreateView, ListsRetrieveUpdateDestroyView

urlpatterns = [
    path("create/lists/", ListsListCreateView.as_view(), name="list-create-list"),
    path(
        "update/lists/<int:pk>/",
        ListsRetrieveUpdateDestroyView.as_view(),
        name="retrieve-update-destroy-list",
    ),
]
