from apps.base_exceptions import BaseEwException


class UserExistException(BaseEwException):
    error_msg = "User already exists error"
    key = "user-already-exists-error"
