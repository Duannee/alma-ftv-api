from django.urls import path

from .views import UserRegisterView, UserUpdateView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("user/update/<int:pk>/", UserUpdateView.as_view(), name="update"),
]
