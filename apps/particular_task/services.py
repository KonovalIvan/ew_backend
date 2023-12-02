from apps.dashboard.selectors import DashboardSelector
from apps.particular_task.models import Task


class TaskServices:
    @staticmethod
    def create_task(data: dict) -> Task:
        dashboard = DashboardSelector.get_by_id(data["dashboard_id"])
        data.update({"dashboard": dashboard})
        return Task.objects.create(**data)
