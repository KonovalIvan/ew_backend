from django.urls import path

from apps.api.projects.view import (
    ActiveProjectsAndTasksView,
    AddProjectView,
    ProjectsShortInfoView,
    SingleProjectView,
)

urlpatterns = [
    path("projects-tasks-active/", ActiveProjectsAndTasksView.as_view(), name="projects-tasks-active"),
    path("projects-short-info/", ProjectsShortInfoView.as_view(), name="projects-short-info"),
    path("<uuid:project_id>/", SingleProjectView.as_view(), name="project-by-id"),
    path("create/", AddProjectView.as_view(), name="new-project"),
    # ---------------------------------------NOT USED YET-------------------------------------------------------------
    # path("active/", ActiveProjectView.as_view(), name="projects-active"),
    # path("finished/", FinishedProjectView.as_view(), name="projects-archived"),
]
