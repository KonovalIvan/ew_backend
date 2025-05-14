from uuid import UUID

from celery import shared_task

from apps.projects.selectors import ProjectSelector


@shared_task()
def task_archiving_project(
    project_id: UUID,
) -> None:
    # TODO: relocate project and all related dashboards and tasks to second, less powerfully database
    if project := ProjectSelector.get_by_id_or_none(project_id):
        if not project.is_archived and project.finished:
            project.is_archived = True
            project.save()
