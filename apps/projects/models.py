from django.db import models

from apps.base_models import BaseModel, TimestampMixin


class BuildingProject(BaseModel, TimestampMixin):
    name = models.CharField(max_length=32, null=False, blank=False)
    address = models.CharField(max_length=128)
    description = models.TextField()
    client = models.CharField(max_length=128)
    designer = models.CharField(max_length=128)
    building_master = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)


    def __str__(self) -> str:
        return f"{self.name}"

    def short_description(self) -> str:
        return self.description[:128]
