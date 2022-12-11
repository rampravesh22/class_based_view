from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from core.forms import LoginForm
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="core/home.html")),
    path("dashboard/", TemplateView.as_view(
        template_name="core/dashboard.html"), name="dashboard"),
    path(
        "login/", auth_views.LoginView.as_view(
            template_name="core/login.html", authentication_form=LoginForm), name="login"),
    path(
        "logout/", auth_views.LogoutView.as_view(
            template_name="core/logout.html"), name="logout"),
    path("change_password/", auth_views.PasswordChangeView.as_view(
        template_name="core/change_pass.html", success_url=reverse_lazy("changepassdone")), name="changepass"),
    path("changepassdone/", auth_views.PasswordChangeDoneView.as_view(
        template_name="core/changepassdone.html"), name="changepassdone")

]
