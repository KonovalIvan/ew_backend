import logging
import uuid
from datetime import timedelta
from typing import Any

from django.db import OperationalError
from django.utils import timezone

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


def celery_apply_async(task: Any, *args: Any, **kwargs: Any) -> CeleryTask:
    # base `countdown` and `eta` params as in apply_async
    countdown = kwargs.pop("countdown", 0)
    eta = kwargs.pop("eta", timezone.now() + timedelta(seconds=countdown))

    scheduled = CeleryTask.objects.create(
        task_name=task.name,
        task_id=kwargs.pop("task_id", f"{uuid.uuid4()}"),
        task_args=args or kwargs.pop("args", []),
        task_kwargs=kwargs.pop("kwargs", {}),
        kwargs=kwargs,
        task_eta=eta,
    )
    if timezone.now() + timedelta(minutes=30) >= eta:
        celery_send_task_queue(scheduled)

    return scheduled


def celery_revoke(tasks_ids: Any) -> None:
    celery_tasks.control.revoke(tasks_ids)
