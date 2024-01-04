from django.urls import include, path

urlpatterns = [
    path("authentication/", include("apps.api.authentication.urls")),
    path("projects/", include("apps.api.projects.urls")),
    path("dashboard/", include("apps.api.dashboard.urls")),
    path("task/", include("apps.api.particular_task.urls")),
    path("comments/", include("apps.api.comments.urls")),
    path("images-asset/", include("apps.api.images.urls")),
]
