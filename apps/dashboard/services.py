from uuid import UUID

from apps.dashboard.models import Dashboard
from apps.dashboard.selectors import DashboardSelector
from apps.projects.selectors import ProjectSelector


class DashboardServices:
    @staticmethod
    def create_dashboard(data: dict) -> Dashboard:
        return Dashboard.objects.create(
            name=data["name"],
            description=data["description"],
            project=ProjectSelector.get_by_id(data["project_id"]),
        )

    @staticmethod
    def update_dashboard(data: dict, dashboard_id: UUID) -> Dashboard:
        dashboard = DashboardSelector.get_all_by_id(id=dashboard_id)
        dashboard.update(**data)
        return dashboard.first()

    @staticmethod
    def delete_single_dashboard_by_id(dashboard_id: UUID) -> bool:
        try:
            dashboard = DashboardSelector.get_by_id(id=dashboard_id)
            dashboard.delete()
            return True
        except Dashboard.DoesNotExist:
            return False
