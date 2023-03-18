from django.urls import path

from apps.api.authentication.views import LoginApiView, UserApiView

urlpatterns = [
    path("user/", UserApiView.as_view(), name="user"),
    path("login/", LoginApiView.as_view(), name="user"),
]
