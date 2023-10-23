from django.contrib import admin

from apps.projects.models import BuildingProject


class BuildingProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(BuildingProject, BuildingProjectAdmin)
