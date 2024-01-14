from django.urls import include, path

from apps.api.authentication.views import (
    LoginView,
    UserDetailsView,
    VerifyTokenView,
    confirm_email,
)

register_urlpatterns = [
    path("confirm-email", confirm_email, name="confirm-email"),
]

urlpatterns = [
    path("user-details/", UserDetailsView.as_view(), name="authentication-user-details"),
    path("login/", LoginView.as_view(), name="authentication-login"),
    path("verify-token/", VerifyTokenView.as_view(), name="verify-token"),
    path("register/", include(register_urlpatterns)),
]
