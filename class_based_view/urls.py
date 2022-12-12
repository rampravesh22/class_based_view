from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views
# from django.views.generic import TemplateView
from django.urls import reverse_lazy
# from core.forms import LoginForm
urlpatterns = [
    path('admin/', admin.site.urls),

    path("", views.Home.as_view()),

    path("register/", views.RegistrationForm.as_view(), name="register"),

    path("dashboard/", views.DashBoard.as_view(), name="dashboard"),

    path("login/", views.CustomLoginView.as_view(), name="login"),

    path("logout/", views.CustomLogoutView.as_view(), name="logout"),

    path("change_password/", views.CustomPasswordChangeView.as_view(
    ), name="changepass"),

    path("changepassdone/", views.CustomPasswordChangeDoneView.as_view(),
         name="changepassdone")

]
