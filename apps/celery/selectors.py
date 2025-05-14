from typing import Optional

from apps.celery.models import CeleryTask


class CeleryTaskSelector:
    @staticmethod
    def get_by_id_or_none(task_id) -> Optional[CeleryTask]:
        try:
            return CeleryTask.objects.get(task_id=task_id)
        except CeleryTask.DoesNotExist:
            return None
