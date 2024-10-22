from django.urls import path
from django.contrib.auth.views import LogoutView
from auth_app.views import index, LoginLPA7User


app_name = "auth"
urlpatterns = [
    path("", index, name="index"),
    path("login/", LoginLPA7User.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
