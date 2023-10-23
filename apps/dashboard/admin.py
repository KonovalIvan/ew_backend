from django.contrib import admin

from apps.dashboard.models import Dashboard


class ProjectDashboardAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dashboard, ProjectDashboardAdmin)
