from django.urls import path
from .views import CustomUserRegisterView


app_name = "users"
urlpatterns = [
    path("signup/", CustomUserRegisterView.as_view(), name="signup"),
]
