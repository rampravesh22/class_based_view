# from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth import views as authviews
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from core.forms import LoginForm

# Create your views here.


class RegistrationForm(CreateView):
    form_class = UserCreationForm
    template_name = "core/register.html"

    success_url = "/register/"

    def form_valid(self, form):
        messages.success(self.request, "Account Created Successully")
        return super().form_valid(form)


class CustomLoginView(authviews.LoginView):
    template_name = "core/login.html"
    authentication_form = LoginForm


class CustomLogoutView(authviews.LogoutView):
    template_name = "core/logout.html"


class CustomPasswordChangeView(authviews.PasswordChangeView):
    template_name = "core/change_pass.html"
    success_url = reverse_lazy("changepassdone")


class CustomPasswordChangeDoneView(authviews.PasswordChangeDoneView):
    template_name = "core/changepassdone.html"
    success_url = reverse_lazy("changepassdone")


class DashBoard(TemplateView):
    template_name = 'core/dashboard.html'


class Home(TemplateView):
    template_name = "core/home.html"
