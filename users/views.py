from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CreateUserForm, CustomAuthenticationForm
from .models import User


class CustomLoginView(LoginView):
    template_name = "users/login.html"
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy("diary:home")


class UserCreateView(CreateView):
    model = User
    form_class = CreateUserForm
    success_url = reverse_lazy("users:login")


class CustomLogoutView(LogoutView):
    template_name = "users/logout.html"
    next_page = reverse_lazy("users:logout")
