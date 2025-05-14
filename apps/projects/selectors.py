from typing import Optional
from uuid import UUID

from django.db.models import Q, QuerySet

from apps.authentication.models import User
from apps.projects.models import Project


class ProjectSelector:
    @staticmethod
    def get_by_id(id: UUID) -> Project:
        return Project.objects.get(id=id)

    @staticmethod
    def get_by_id_or_none(id: UUID) -> Optional[Project]:
        try:
            return Project.objects.get(id=id)
        except Project.DoesNotExist:
            return None

    @staticmethod
    def get_all_by_user(user: User, is_archived: bool = False) -> QuerySet[Project]:
        projects = Project.objects.filter(Q(client=user) | Q(designer=user) | Q(building_master=user))
        return projects.filter(is_archived=is_archived)

    @staticmethod
    def get_active_by_user(user: User) -> QuerySet[Project]:
        return Project.objects.filter(Q(client=user) | Q(designer=user) | Q(building_master=user), finished=False)

    @staticmethod
    def get_archived_by_user(user: User) -> QuerySet[Project]:
        return Project.objects.filter(Q(client=user) | Q(designer=user) | Q(building_master=user), finished=True)
