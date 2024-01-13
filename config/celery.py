import os
from typing import List

from celery import Celery
from dotenv import load_dotenv

from config.settings import SECRETS_DIR

load_dotenv(os.path.join(SECRETS_DIR, ".env.celery"))
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def task_discover() -> List[str]:
    task_dirs = []
    apps_path = os.path.join(
        project_root,
        "apps",
    )
    for directory in os.listdir(apps_path):
        app_directory = os.path.join(apps_path, directory)
        file_path = os.path.join(app_directory, "tasks.py")
        if os.path.isdir(app_directory) and directory not in ["api", "__pycache__"]:
            if os.path.isfile(file_path):
                edited_file_path = (
                    f"app{file_path.replace(project_root, '').replace('.py', '').replace(os.path.sep, '.')}"
                )
                task_dirs.append(edited_file_path)

    return task_dirs


# Check that DJANGO_SETTINGS_MODULE available from `settings.py` file
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

celery_tasks = Celery("ew_backend")
celery_tasks.config_from_object("django.conf:settings", namespace="CELERY")

celery_tasks.conf.broker_url = os.getenv("CELERY_BROKER_URL")
celery_tasks.conf.result_backend = os.getenv("CELERY_RESULT_BACKEND")
celery_tasks.conf.timezone = os.getenv("CELERY_TIMEZONE")
celery_tasks.autodiscover_tasks(task_discover)
