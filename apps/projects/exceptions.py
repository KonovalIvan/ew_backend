from apps.base_exceptions import BaseEwException


class ProjectDoesntExistException(BaseEwException):
    error_msg = "Project with passed id does not exist"
    key = "project-doesnt-exists-error"
