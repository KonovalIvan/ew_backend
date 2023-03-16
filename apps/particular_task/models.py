from django.db import models

from apps.authentication.models import User
from apps.base_models import BaseModel, TimestampMixin
from apps.dashboard.models import ProjectDashboard
from apps.particular_task.consts import image_directory_path


class ParticularTask(BaseModel, TimestampMixin):
    name = models.CharField(max_length=32, null=False, blank=False)
    description = models.TextField()
    dashboard = models.ForeignKey(ProjectDashboard,
                                  on_delete=models.SET_NULL,
                                  related_name='task',
                                  blank=True,
                                  null=True)
    status = models.BooleanField(default=False)
    client_accepting = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=image_directory_path(dashboard=dashboard))

    # TODO: create deleted_user logic and replace set_null to deleted user
    assign = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='task', null=True, blank=True)


    def __str__(self) -> str:
        return f"{self.name}"

    def short_description(self) -> str:
        return self.description[:128]
