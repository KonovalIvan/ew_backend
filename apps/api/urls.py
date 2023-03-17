from django.urls import include, path

urlpatterns = [
    path("authentication/", include("apps.api.authentication.urls")),
]
