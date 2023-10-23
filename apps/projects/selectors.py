from uuid import UUID

from django.db.models import Q, QuerySet

from apps.authentication.models import User
from apps.projects.models import Project


class ProjectSelector:
    @staticmethod
    def get_by_id(id: UUID) -> Project:
        return Project.objects.get(id=id)

    @staticmethod
    def get_all_by_user(user: User) -> QuerySet[Project]:
        return Project.objects.filter(Q(client=user) | Q(designer=user) | Q(building_master=user))

    @staticmethod
    def get_active_by_user(user: User) -> QuerySet[Project]:
        return Project.objects.filter(Q(client=user) | Q(designer=user) | Q(building_master=user), finished=False)

    @staticmethod
    def get_archived_by_user(user: User) -> QuerySet[Project]:
        return Project.objects.filter(Q(client=user) | Q(designer=user) | Q(building_master=user), finished=True)
