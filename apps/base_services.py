import uuid


def generate_random_filename_for_project(instance, filename: str):
    project_id = instance.id if not hasattr(instance, "project") else instance.project.id
    task_id = None if not hasattr(instance, "task") else f"/tasks/{instance.task.id}"
    return f"projects/{project_id}{task_id}/{uuid.uuid4().hex[:10]}-{filename}"


def generate_random_filename_for_user_avatar(instance, filename: str):
    user_id = instance.id if not hasattr(instance, "user") else instance.user.id
    return f"users/{user_id}/avatar/{uuid.uuid4().hex[:10]}-{filename}"
