import logging
from typing import Any

from django.db import OperationalError

from apps.celery.models import CeleryTask
from config import celery_tasks

log = logging.getLogger(__name__)


def celery_send_task_queue(task: CeleryTask) -> None:
    try:
        celery_tasks.send_task(
            name=task.task_name,
            task_id=task.task_id,
            args=task.task_args,
            kwargs=task.task_kwargs,
            eta=task.task_eta,
        )
    except OperationalError:
        log.exception(f"Could not send celery task to the queue. {task.id}")


def celery_revoke(tasks_ids: Any) -> None:
    celery_tasks.control.revoke(tasks_ids)
