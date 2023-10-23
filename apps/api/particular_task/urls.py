from django.urls import path

from apps.api.particular_task.view import SingleTaskView, TaskView

# ---------------------------------------NOT USED YET-------------------------------------------------------------

urlpatterns = [
    path("<uuid:dashboard_id>/", TaskView.as_view(), name="task-by-dashboard-id"),
    path("<uuid:dashboard_id>/", TaskView.as_view(), name="task-by-dashboard-id"),
    path("<uuid:task_id>/details", SingleTaskView.as_view(), name="task-details"),
]
