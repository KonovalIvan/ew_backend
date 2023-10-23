from uuid import UUID

from django.db.models import QuerySet

from apps.dashboard.models import Dashboard
from apps.projects.models import Project


class DashboardSelector:
    @staticmethod
    def get_by_id(id: UUID) -> Dashboard:
        return Dashboard.objects.get(id=id)

    @staticmethod
    def get_all_by_project(project: Project) -> QuerySet[Dashboard]:
        return Dashboard.objects.filter(project=project)
