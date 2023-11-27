from django.db import models

from apps.authentication.models import User
from apps.base_models import BaseModel, TimestampMixin
from apps.dashboard.models import Dashboard
from apps.particular_task.consts import image_directory_path


class Task(BaseModel, TimestampMixin):
    """
    Model created as card for dashboard
    """

    name = models.CharField(max_length=32, null=False, blank=False)
    description = models.TextField()
    dashboard = models.ForeignKey(
        Dashboard,
        on_delete=models.SET_NULL,
        related_name="task",
        blank=True,
        null=True,
    )
    finished = models.BooleanField(default=False)
    client_accepting = models.BooleanField(default=False)
    photo = models.ImageField(
        upload_to=image_directory_path(dashboard=dashboard),
        null=True,
        blank=True,
    )  # type: ignore

    # TODO: create deleted_user logic and replace set_null to deleted user
    assign = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="task_assign",
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="task_owner",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    def short_description(self) -> str:
        return self.description[:128]
