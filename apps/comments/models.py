from django.db import models

from apps.authentication.models import User
from apps.base_models import BaseModel, TimestampMixin
from apps.particular_task.models import Task


class Comments(BaseModel, TimestampMixin):
    """
    Model for comments from people who will check how the tasks are going
    """

    description = models.TextField()
    task = models.ForeignKey(Task, related_name="comments", on_delete=models.CASCADE, blank=True, null=True)
    comments = models.ForeignKey("self", null=True, blank=True, related_name="replies", on_delete=models.CASCADE)
    creator = models.ForeignKey(User, editable=False, null=True, blank=True, on_delete=models.SET_NULL)

    def short_description(self) -> str:
        return f"{self.description[:125]}{'...' if len(self.description) > 125 else ''}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None) -> None:
        if self.task is not None and self.comments is not None:
            raise ValueError("One field must be empty")
        elif self.comments is None and self.task is None:
            raise ValueError("Related Task or Comment is required")
        super(Comments, self).save()
