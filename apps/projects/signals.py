from datetime import timedelta
from typing import Any

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone

from apps.celery.selectors import CeleryTaskSelector
from apps.celery.utils import celery_apply_async, celery_revoke
from apps.projects.consts import ARCHIVING_TIME_DAYS
from apps.projects.models import Project
from apps.projects.tasks import task_archiving_project


@receiver(pre_delete, sender=Project)
def user_unmark_contractor_on_edit(sender: Project, instance: Project, *args: Any, **kwargs: Any) -> None:
    if instance.address:
        instance.address.delete()


@receiver(post_save, sender=Project)
def user_unmark_contractor_on_edit1(sender: Project, instance: Project, *args: Any, **kwargs: Any) -> None:
    if instance.finished is True and instance.is_archived is False:
        task_id = f"celery_archiving_project--{instance.id}"
        if task := CeleryTaskSelector.get_by_id_or_none(task_id=task_id):
            celery_revoke(tasks_ids=task_id)
            task.delete()
        celery_apply_async(
            task_archiving_project,
            task_id=task_id,
            args=[instance.id],
            eta=timezone.now() + timedelta(days=ARCHIVING_TIME_DAYS),
        )
