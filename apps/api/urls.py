from django.urls import path, include
from apps.api.authentication.views import (
    UserApiView,
)

urlpatterns = [
    path("authentication/", include("apps.api.authentication.urls")),
]
