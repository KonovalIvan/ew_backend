from apps.base_exceptions import BaseEwException


class UserExistException(BaseEwException):
    error_msg = "User with this email already exists"
    key = "user-already-exists-error"


class UserNotFoundException(BaseEwException):
    error_msg = "User not found"
    key = "user-not-found-error"


class TokenNotFoundException(BaseEwException):
    error_msg = "Token not found"
    key = "token-not-found-error"
