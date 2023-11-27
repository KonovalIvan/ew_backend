from django.apps import AppConfig


class ConfigAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "config"

    def ready(self):
        from apps.images import signals as images_signals  # noqa
        from apps.projects import signals as projects_signals  # noqa
