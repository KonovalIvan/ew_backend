from uuid import UUID

from apps.authentication.models import User
from apps.particular_task.models import Task
from apps.particular_task.selectors import TaskSelector


class TaskServices:
    @staticmethod
    def create_task(data: dict, creator: User) -> Task:
        data["owner"] = creator
        return Task.objects.create(**data)

    @staticmethod
    def delete_task_by_id(task_id: UUID) -> bool:
        try:
            task = TaskSelector.get_by_id(id=task_id)
            task.delete()
            return True
        except Task.DoesNotExist:
            return False

    @staticmethod
    def update_task(data: dict, task_id: UUID) -> Task:
        task = TaskSelector.filter_by_id(id=task_id)
        task.update(**data)
        return task.first()
