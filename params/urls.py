from django.urls import path

from .views import (
    ParamsCreateView,
    ParamsRetrieveUpdateDestroyView,
    ParamsListView,
)

urlpatterns = [
    path(
        "create/params/",
        ParamsCreateView.as_view(),
        name="create-params",
    ),
    path("list/params/", ParamsListView.as_view(), name="list-params"),
    path(
        "update/params/<int:pk>/",
        ParamsRetrieveUpdateDestroyView.as_view(),
        name="retrieve-update-destroy-params",
    ),
]
