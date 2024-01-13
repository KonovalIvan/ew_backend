from django.urls import include, path

from apps.api.authentication.views import (
    ConfirmEmailView,
    LoginView,
    UserDetailsView,
    VerifyTokenView,
)

register_urlpatterns = [
    path("confirm-email", ConfirmEmailView.as_view(), name="confirm-email"),
]

urlpatterns = [
    path("user-details/", UserDetailsView.as_view(), name="authentication-user-details"),
    path("login/", LoginView.as_view(), name="authentication-login"),
    path("verify-token/", VerifyTokenView.as_view(), name="verify-token"),
    path("register/", include(register_urlpatterns)),
]
