from django.urls import path

from apps.api.authentication.views import LoginView, UserDetailsView, VerifyTokenView

urlpatterns = [
    path("user-details/", UserDetailsView.as_view(), name="authentication-user-details"),
    path("login/", LoginView.as_view(), name="authentication-login"),
    path("verify-token/", VerifyTokenView.as_view(), name="verify-token"),
    # ---------------------------------------NOT USED YET-------------------------------------------------------------
    # path("register-user/", RegisterUserView.as_view(), name="authentication-register-user"),
]
