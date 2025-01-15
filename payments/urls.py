from django.urls import path

from .views import (
    PaymentCreateView,
    PaymentListView,
    PaymentRetrieveUpdateDestroyView,
)

urlpatterns = [
    path(
        "create/payment/", PaymentCreateView.as_view(), name="create-payment"
    ),
    path("list/payment/", PaymentListView.as_view(), name="list-payment"),
    path(
        "update/payment/<int:pk>/",
        PaymentRetrieveUpdateDestroyView.as_view(),
        name="retrieve-update-destroy-payment",
    ),
]
