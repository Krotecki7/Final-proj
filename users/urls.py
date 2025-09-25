from django.urls import path

from users.apps import UsersConfig
from .views import CustomLoginView, UserCreateView, CustomLogoutView

app_name = UsersConfig.name

urlpatterns = [
    path("login/",
         CustomLoginView.as_view(template_name="login.html"),
         name="login"),
    path("register/", UserCreateView.as_view(template_name="user_form.html"), name="register"),
    path("logout/", CustomLogoutView.as_view(next_page="users:logout", template_name="logout.html"), name="logout"),
]
