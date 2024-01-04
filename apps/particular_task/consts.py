from apps.dashboard.models import Dashboard


def image_directory_path(dashboard: Dashboard) -> str:
    return "uploads/dashboard/{0}".format(dashboard.name)
