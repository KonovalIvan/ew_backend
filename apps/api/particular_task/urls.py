from django.urls import path

from apps.api.particular_task.view import NewTaskView, SingleTaskView

urlpatterns = [
    path("create/", NewTaskView.as_view(), name="task-by-dashboard-id"),
    path("<uuid:task_id>/", SingleTaskView.as_view(), name="task-by-id"),
    # ---------------------------------------NOT USED YET-------------------------------------------------------------
    # path("<uuid:dashboard_id>/", TaskView.as_view(), name="task-by-dashboard-id"),
    # path("<uuid:dashboard_id>/", TaskView.as_view(), name="task-by-dashboard-id"),
    # path("<uuid:task_id>/details", SingleTaskView.as_view(), name="task-details"),
]
