from django.urls import path

from apps.api.projects.view import ProjectApiView

urlpatterns = [
    path("all/", ProjectApiView.as_view(), name="user"),
]
