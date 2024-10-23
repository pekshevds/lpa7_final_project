from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from auth_app.models import LPA7User


class LPA7UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = get_user_model()
        fields = ["email"]

    def clean_password2(self) -> str:
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit: bool = True) -> LPA7User:
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class LPA7UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ["is_active", "is_admin"]

    def save(self, commit: bool = True) -> LPA7User:
        user = super().save(commit=False)
        user.is_active = self.cleaned_data.get("is_active", user.is_active)
        user.is_admin = self.cleaned_data.get("is_admin", user.is_admin)
        if commit:
            user.save()
        return user


class LoginLPA7UserForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "password"]
