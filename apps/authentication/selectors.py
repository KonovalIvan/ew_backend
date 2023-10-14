from apps.authentication.models import User


class UserSelector:
    @staticmethod
    def get_by_username(username: str) -> User:
        return User.objects.get(username=username)
