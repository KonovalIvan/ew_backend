from typing import Optional
from uuid import UUID

from apps.authentication.models import Address, User, RegistrationToken


class UserSelector:

    @staticmethod
    def get_by_id(id: UUID) -> Optional[User]:
        return User.objects.get(id=id)

    @staticmethod
    def get_by_username(username: str) -> User:
        return User.objects.get(username=username.lower())

    @staticmethod
    def get_by_username_or_none(username: str) -> Optional[User]:
        try:
            return User.objects.get(username=username.lower())
        except User.DoesNotExist:
            return None


class RegistrationTokenSelector:
    @staticmethod
    def get_by_id_and_user(id: UUID, user: User) -> Optional[RegistrationToken]:
        return RegistrationToken.objects.get(id=id, user=user)


class AddressSelector:
    @staticmethod
    def get_by_id_or_none(id: UUID) -> Optional[Address]:
        try:
            return Address.objects.get(id=id)
        except User.DoesNotExist:
            return None
