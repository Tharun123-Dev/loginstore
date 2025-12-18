from django.urls import path
from .views import signup_api, login_api

urlpatterns = [
    path("api/signup/", signup_api),
    path("api/login/", login_api),
]
