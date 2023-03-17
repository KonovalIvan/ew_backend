from django.urls import path
from apps.api.authentication.views import (
    UserApiView,
)

urlpatterns = [
    path("user/", UserApiView.as_view(), name="user"),
]
