from apps.base_exceptions import BaseEwException


class UserExistException(BaseEwException):
    error_msg = "User with this email already exists error"
    key = "user-already-exists-error"
