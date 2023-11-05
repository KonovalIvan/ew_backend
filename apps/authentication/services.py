from typing import Optional, Tuple

from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.authtoken.models import Token
from rest_framework.request import Request

from apps.authentication.exceptions import UserExistException
from apps.authentication.models import Address, User
from apps.authentication.selectors import UserSelector


class BearerAuthentication(TokenAuthentication):
    keyword = "Bearer"

    def authenticate_credentials(self, key: str) -> tuple[User, Token]:
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed("Invalid token")

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed("User inactive or deleted")

        return token.user, token

    def authenticate(self, request: Request) -> Optional[Tuple[User, Token]]:
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1 or len(auth) > 2:
            raise exceptions.AuthenticationFailed("Invalid token header.")

        try:
            token = auth[1].decode()
        except UnicodeError:
            raise exceptions.AuthenticationFailed(
                "Invalid token header. Token string should not contain invalid characters."
            )

        return self.authenticate_credentials(token)

    def authenticate_header(self, request: Request) -> str:
        return self.keyword


class AuthenticationServices:
    @staticmethod
    def create_user(user_data: dict) -> User:
        email = user_data["email"]
        if UserSelector.get_by_username_or_none(email):
            raise UserExistException

        user = User.objects.create(
            username=email,
            email=email,
        )
        user.set_password(user_data["password"])
        user.save()

        return user


class AddressServices:
    @staticmethod
    def create_address(address_data: dict) -> Address:
        # TODO: Add validators for creating address
        address = Address.objects.create(
            address_line_1=address_data["address_line_1"],
            address_line_2=getattr(address_data["address_line_2"], ""),
            post_code=address_data["post_code"],
            city=address_data["city"],
            country=address_data["country"],
        )
        return address
