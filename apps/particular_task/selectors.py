from uuid import UUID

from django.db.models import QuerySet

from apps.dashboard.models import Dashboard
from apps.particular_task.models import Task


class TaskSelector:
    @staticmethod
    def get_by_id(id: UUID) -> Task:
        return Task.objects.get(id=id)

    @staticmethod
    def get_all_by_dashboard(dashboard: Dashboard) -> QuerySet[Task]:
        return Task.objects.filter(dashboard=dashboard)
