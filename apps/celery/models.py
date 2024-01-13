from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.db.models import JSONField

from apps.base_models import BaseModel, TimestampMixin


class CeleryTask(BaseModel, TimestampMixin):
    """Model for cashing celery task data"""

    task_id = models.TextField(null=True, blank=True)
    task_name = models.TextField(max_length=256)
    task_args = JSONField(blank=True, null=True, encoder=DjangoJSONEncoder)
    task_kwargs = JSONField(blank=True, null=True, encoder=DjangoJSONEncoder)
    task_eta = models.DateTimeField()

    kwargs = JSONField(null=True, blank=True, encoder=DjangoJSONEncoder)
