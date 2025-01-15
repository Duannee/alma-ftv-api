from django.urls import path

from .views import CoachListCreateView, CoachRetrieveUpdateDestroyView

urlpatterns = [
    path(
        "create/coaches/",
        CoachListCreateView.as_view(),
        name="list-create-coaches",
    ),
    path(
        "update/coaches/<int:pk>/",
        CoachRetrieveUpdateDestroyView.as_view(),
        name="retrieve-update-destroy-coaches",
    ),
]
