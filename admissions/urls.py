from django.urls import path

from .views import AdmissionListView, ApproveAdmissionView, RejectAdmissionView

urlpatterns = [
    path("admissions/", AdmissionListView.as_view(), name="list-admissions"),
    path(
        "admissions/approve/<int:pk>/",
        ApproveAdmissionView.as_view(),
        name="approve-admission",
    ),
    path(
        "admissions/reject/<int:pk>/",
        RejectAdmissionView.as_view(),
        name="reject-admission",
    ),
]
