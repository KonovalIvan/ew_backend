from django.contrib import admin

from apps.particular_task.models import ParticularTask


class ParticularTaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(ParticularTask, ParticularTaskAdmin)
