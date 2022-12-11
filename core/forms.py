from django import forms
from core.models import Student
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={"class": "myclass", "id": "myname_id"}),
            'roll': forms.TextInput(attrs={"class": "myclass"})
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, "class": "myclass"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', "class": "myclass"}),
    )
