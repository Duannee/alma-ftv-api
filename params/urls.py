from django.urls import path

from .views import ParamsListCreateView, ParamsRetrieveUpdateDestroyView

urlpatterns = [
    path(
        "create/params/",
        ParamsListCreateView.as_view(),
        name="list-create-params",
    ),
    path(
        "update/params/<int:pk>/",
        ParamsRetrieveUpdateDestroyView.as_view(),
        name="retrieve-update-destroy-params",
    ),
]
