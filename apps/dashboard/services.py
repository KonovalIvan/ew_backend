from apps.dashboard.models import Dashboard
from apps.projects.selectors import ProjectSelector


class DashboardServices:
    @staticmethod
    def create_dashboard(data: dict) -> Dashboard:
        return Dashboard.objects.create(
            name=data["name"],
            description=data["description"],
            project=ProjectSelector.get_by_id(data["project_id"]),
        )
