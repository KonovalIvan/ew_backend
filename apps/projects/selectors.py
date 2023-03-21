from uuid import UUID

from django.db.models import QuerySet

from apps.authentication.models import User
from apps.projects.models import BuildingProject


class ProjectSelector:
    @staticmethod
    def get_by_id(id: UUID) -> BuildingProject:
        return BuildingProject.objects.get(id=id)

    @staticmethod
    def get_all_by_owner(owner: User) -> QuerySet[BuildingProject]:
        return BuildingProject.objects.filter(owner=owner)

    @staticmethod
    def get_active_by_owner(owner: User) -> QuerySet[BuildingProject]:
        return BuildingProject.objects.filter(owner=owner, finished=False)

    @staticmethod
    def get_archived_by_owner(owner: User) -> QuerySet[BuildingProject]:
        return BuildingProject.objects.filter(owner=owner, finished=True)
