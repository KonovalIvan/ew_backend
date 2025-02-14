from django.db import models

from apps.base_models import BaseModel, TimestampMixin
from apps.projects.models import Project


class Dashboard(BaseModel, TimestampMixin):
    """
    This model created as a place to which the user, owner, principal and td will have access.
    Created to see project progress
    """

    name = models.CharField(max_length=64, null=False, blank=False)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="dashboard",
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    def short_description(self) -> str:
        return self.description[:128]
