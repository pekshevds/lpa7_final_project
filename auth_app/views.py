from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView
from auth_app.forms import LoginLPA7UserForm


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request, template_name="auth_app\index.html", context={"user": request.user}
    )


class LoginLPA7User(LoginView):
    form_class = LoginLPA7UserForm
    template_name = "auth_app/login.html"
