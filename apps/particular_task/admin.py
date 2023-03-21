from django.contrib import admin

from apps.particular_task.models import Task


class ParticularTaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task, ParticularTaskAdmin)
