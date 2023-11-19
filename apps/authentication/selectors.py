from typing import Optional
from uuid import UUID

from apps.authentication.models import Address, User


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


class AddressSelector:
    @staticmethod
    def get_by_id_or_none(id: UUID) -> Optional[Address]:
        try:
            return Address.objects.get(id=id)
        except User.DoesNotExist:
            return None
