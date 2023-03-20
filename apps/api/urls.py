from django.urls import include, path

urlpatterns = [
    path("authentication/", include("apps.api.authentication.urls")),
    path("projects/", include("apps.api.projects.urls")),
]
