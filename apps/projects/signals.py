from typing import Any

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from apps.projects.models import Project


@receiver(pre_delete, sender=Project)
def user_unmark_contractor_on_edit(sender: Project, instance: Project, *args: Any, **kwargs: Any) -> None:
    if instance.address:
        instance.address.delete()
