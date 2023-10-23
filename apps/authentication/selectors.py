from typing import Optional

from apps.authentication.models import User


class UserSelector:
    @staticmethod
    def get_by_username(username: str) -> User:
        return User.objects.get(username=username.lower())

    @staticmethod
    def get_by_username_or_none(username: str) -> Optional[User]:
        try:
            return User.objects.get(username=username.lower())
        except User.DoesNotExist:
            return None
