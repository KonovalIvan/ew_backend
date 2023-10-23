from django.contrib import admin

from apps.projects.models import Project, ProjectGallery


class ProjectGalleryInline(admin.TabularInline):
    model = ProjectGallery
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ("designer",)
    inlines = [
        ProjectGalleryInline,
    ]

    def save_model(self, request, obj, form, change):
        if not obj.designer:
            obj.designer = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectGallery)
