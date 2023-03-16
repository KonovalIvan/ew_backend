from django.db import models

from apps.base_models import BaseModel, TimestampMixin
from apps.particular_task.models import ParticularTask


class Commentary(BaseModel, TimestampMixin):
    description = models.TextField()
    task = models.ForeignKey(ParticularTask, related_name='commentary', on_delete=models.CASCADE)
    commentary = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.short_description}"

    def short_description(self) -> str:
        return self.description[:128]
