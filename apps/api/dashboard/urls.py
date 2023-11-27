from django.urls import path

from apps.api.dashboard.view import AddDashboardsView, SingleDashboardsView

urlpatterns = [
    path("create/", AddDashboardsView.as_view(), name="new-dashboard"),
    path("<uuid:dashboard_id>/", SingleDashboardsView.as_view(), name="dashboard-by-id"),
    # ---------------------------------------NOT USED YET-------------------------------------------------------------
    # path("<uuid:project_id>/", DashboardsView.as_view(), name="dashboard-by-project-id"),
    path("<uuid:dashboard_id>/details/", SingleDashboardsView.as_view(), name="dashboard-details-by-id"),
]
