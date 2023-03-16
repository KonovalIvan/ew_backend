from django.contrib import admin

from apps.dashboard.models import ProjectDashboard


class ProjectDashboardAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProjectDashboard, ProjectDashboardAdmin)
