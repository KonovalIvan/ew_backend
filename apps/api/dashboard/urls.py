from django.urls import path

from apps.api.dashboard.view import DashboardsView, SingleDashboardsView

urlpatterns = [
    path("<uuid:project_id>/", DashboardsView.as_view(), name="dashboard-by-project-id"),
    path("<uuid:dashboard_id>/details/", SingleDashboardsView.as_view(), name="dashboard-details-by-id"),
]
