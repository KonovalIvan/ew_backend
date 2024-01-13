import uuid


def generate_random_filename_for_project(instance, filename: str):
    # TODO: change upload task files to projects/{id}/tasks/{id}/name or projects/{id}/name
    path_name = (
        f"projects/{instance.project.id}" if instance.project else f"tasks/{instance.task.id}" if instance.task else ""
    )
    return f"{path_name}/{uuid.uuid4().hex[:10]}-{filename}"


def generate_random_filename_for_user_avatar(instance, filename: str):
    user_id = instance.id if not hasattr(instance, "user") else instance.user.id
    return f"users/{user_id}/avatar/{uuid.uuid4().hex[:10]}-{filename}"
