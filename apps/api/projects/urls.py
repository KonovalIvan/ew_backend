from django.urls import path

from apps.api.projects.view import (
    ActiveProjectsAndTasksView,
    ActiveProjectView,
    FinishedProjectView,
    SingleProjectView,
)

urlpatterns = [
    path("projects-tasks-active/", ActiveProjectsAndTasksView.as_view(), name="projects-tasks-active"),
    # ---------------------------------------NOT USED YET-------------------------------------------------------------
    path("active/", ActiveProjectView.as_view(), name="projects-active"),
    path("<uuid:project_id>/", SingleProjectView.as_view(), name="projects-by-id"),
    path("finished/", FinishedProjectView.as_view(), name="projects-archived"),
]
