from django.db import models

from apps.base_models import BaseModel, TimestampMixin
from apps.base_services import generate_random_filename_for_project
from apps.projects.models import Project


class ImageAsset(BaseModel, TimestampMixin):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="image_gallery",
    )
    image = models.ImageField(
        upload_to=generate_random_filename_for_project,
        null=True,
        blank=True,
    )
