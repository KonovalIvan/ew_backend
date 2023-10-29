from django.db import models

from apps.authentication.models import Address, User
from apps.base_models import BaseModel, TimestampMixin
from apps.base_services import generate_random_filename_for_project


class Project(BaseModel, TimestampMixin):
    # TODO: Add progress field and signal auto update when task finished
    name = models.CharField(max_length=32, null=False, blank=False)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    main_image = models.ImageField(
        upload_to=generate_random_filename_for_project,
    )
    client = models.CharField(max_length=20, null=True, blank=True)
    designer = models.ForeignKey(
        User,
        help_text="Person who create this project",
        related_name="designer_project",
        on_delete=models.SET_NULL,
        editable=False,
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
    finished = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    def short_description(self) -> str:
        return self.description[:128] if self.description else "No description"
