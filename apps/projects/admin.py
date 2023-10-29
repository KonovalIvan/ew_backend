from django.contrib import admin

from apps.images.admin import ImageAssetInline
from apps.projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("designer",)
    inlines = [
        ImageAssetInline,
    ]

    def save_model(self, request, obj, form, change):
        if not obj.designer:
            obj.designer = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Project, ProjectAdmin)
