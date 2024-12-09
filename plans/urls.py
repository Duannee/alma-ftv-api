from django.urls import path
from .views import StudentPlanListCreateView, StudentPlanRetrieveUpdateDestroyView

urls_patterns = [
    path(
        "create/plans/", StudentPlanListCreateView.as_view(), name="list-create-plans"
    ),
    path(
        "update/plans/",
        StudentPlanRetrieveUpdateDestroyView.as_view(),
        name="retrieve-update-destroy-plans",
    ),
]
