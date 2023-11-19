import uuid

from apps.authentication.models import User
from apps.authentication.services import AddressServices
from apps.particular_task.selectors import TaskSelector
from apps.projects.models import Project
from apps.projects.selectors import ProjectSelector


class ProjectsServices:
    @staticmethod
    def get_count_of_active_projects_and_tasks(user: User) -> tuple[int, int]:
        active_tasks = TaskSelector.get_active_by_user(user=user)
        active_projects = ProjectSelector.get_active_by_user(user=user)

        return active_projects.count() if active_projects else 0, active_tasks.count() if active_tasks else 0

    @staticmethod
    def delete_single_project_by_id(project_id: uuid) -> bool:
        try:
            project = ProjectSelector.get_by_id(id=project_id)
            project.delete()
            return True
        except Project.DoesNotExist:
            return False

    @staticmethod
    def create_project(data: dict) -> Project:
        address = None
        if "address" in data:
            address = AddressServices.create_address(address_data=data["address"])
        designer = User.objects.filter(username=data["designer_email"]).first()
        master = User.objects.filter(username=data["building_master_email"]).first()
        return Project.objects.create(
            name=data["name"],
            address=address,
            description=data["description"],
            client=data["client_phone"],
            designer=designer,
            building_master=master,
            finished=False,
        )

    @staticmethod
    def update_project(data: dict, project_id: uuid.UUID) -> Project:
        project = ProjectSelector.get_by_id(id=project_id)
        if "address" in data:
            address = AddressServices.update_address(address_data=data["address"])
            project.address = address

        project.designer = User.objects.filter(username=data["designer_email"]).first()
        project.building_master = User.objects.filter(username=data["building_master_email"]).first()
        project.name = data["name"]
        project.description = data["description"]
        project.client = data["client_phone"]
        project.save()

        return project
