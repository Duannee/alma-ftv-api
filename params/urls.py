from django.urls import path
from .views import ParamsListCreateView, ParamsRetrieveUpdateDestroyView

urls_patterns = [
    path("create/params/", ParamsListCreateView.as_view(), name="list-create-params"),
    path(
        "update/params/<int:pk>",
        ParamsListCreateView.as_view(),
        name="retrieve-update-destroy-params",
    ),
]
