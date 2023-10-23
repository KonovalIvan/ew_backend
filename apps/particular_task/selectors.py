from uuid import UUID

from django.db.models import QuerySet

from apps.authentication.consts import UserType
from apps.authentication.models import User
from apps.dashboard.models import Dashboard
from apps.particular_task.models import Task


class TaskSelector:
    @staticmethod
    def get_by_id(id: UUID) -> Task:
        return Task.objects.get(id=id)

    @staticmethod
    def get_all_by_dashboard(dashboard: Dashboard) -> QuerySet[Task]:
        return Task.objects.filter(dashboard=dashboard)

    @staticmethod
    def get_active_by_user(user: User) -> QuerySet[Task]:
        if user.user_type == UserType.DESIGNER.value:
            return Task.objects.filter(owner=user, finished=False)
        elif user.user_type == UserType.WORKER.value:
            return Task.objects.filter(assign=user, finished=False)
