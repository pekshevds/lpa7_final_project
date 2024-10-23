from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from auth_app.forms import LoginLPA7UserForm, LPA7UserCreationForm, LPA7UserChangeForm
from auth_app.models import LPA7User


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        template_name="auth_app/index.html",
        context={"users": LPA7User.objects.all(), "current_user": request.user},
    )


class LoginLPA7User(LoginView):
    form_class = LoginLPA7UserForm
    template_name = "auth_app/login.html"


class CreateLPA7User(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request,
            template_name="auth_app/create.html",
            context={"form": LPA7UserCreationForm()},
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        user_form = LPA7UserCreationForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse("auth:index"))
        return HttpResponseRedirect(reverse("auth:create"))


class ChangeLPA7User(LoginView):
    def get(self, request: HttpRequest, email: str) -> HttpResponse:
        user = get_object_or_404(LPA7User, email=email)
        user_form = LPA7UserChangeForm(instance=user)
        return render(
            request,
            template_name="auth_app/change.html",
            context={"form": user_form, "user": user},
        )

    def post(self, request: HttpRequest, email: str) -> HttpResponse:
        user = get_object_or_404(LPA7User, email=email)
        user_form = LPA7UserChangeForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
        return HttpResponseRedirect(reverse("auth:index"))
