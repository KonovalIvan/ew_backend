from django.db import models

from apps.authentication.models import User
from apps.base_models import BaseModel, TimestampMixin
from apps.dashboard.models import Dashboard


class Task(BaseModel, TimestampMixin):
    """
    Model created as card for dashboard
    """

    name = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    dashboard = models.ForeignKey(
        Dashboard,
        on_delete=models.CASCADE,
        related_name="task",
        blank=True,
        null=True,
    )
    finished = models.BooleanField(default=False)
    client_accepting = models.BooleanField(default=False)

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
