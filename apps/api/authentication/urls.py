from django.urls import path

from apps.api.authentication.views import LoginView, RegisterUserView, UserDetailsView

urlpatterns = [
    path("user-details/", UserDetailsView.as_view(), name="authentication-user-details"),
    path("register-user/", RegisterUserView.as_view(), name="authentication-register-user"),
    path("login/", LoginView.as_view(), name="authentication-login"),
]
