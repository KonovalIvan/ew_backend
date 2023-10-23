import uuid


def generate_random_filename_for_project(instance, filename: str):
    project_id = instance.id if not hasattr(instance, "project") else instance.project.id
    return f"{project_id}/{uuid.uuid4().hex[:10]}-{filename}"
