from django.urls import path
from .views import CreateCoachView

urlpatterns = [
    path("create/coaches/", CreateCoachView.as_view(), name="create-coaches")
]
