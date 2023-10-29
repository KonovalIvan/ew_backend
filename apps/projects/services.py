import uuid

from apps.authentication.models import User
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
    def delete_single_project_by_id(project_id: uuid):
        try:
            project = ProjectSelector.get_by_id(id=project_id)
            project.delete()
            return True
        except Project.DoesNotExist:
            return False
