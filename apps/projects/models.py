from django.db import models

from apps.authentication.models import Address, User
from apps.base_models import BaseModel, TimestampMixin


class BuildingProject(BaseModel, TimestampMixin):
    name = models.CharField(max_length=32, null=False, blank=False)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    client = models.ForeignKey(
        User,
        related_name="user_project",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    designer = models.ForeignKey(
        User,
        related_name="designer_project",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    building_master = models.ForeignKey(
        User,
        related_name="master_project",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        User,
        help_text="Company realized this project",
        related_name="owner_project",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    finished = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    def short_description(self) -> str:
        return self.description[:128] if self.description else "No description"
