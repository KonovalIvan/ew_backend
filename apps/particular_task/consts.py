from apps.dashboard.models import ProjectDashboard


def image_directory_path(dashboard: ProjectDashboard) -> str:
    return "uploads/dashboard/{0}".format(dashboard.name)
