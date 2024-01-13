from django.db import transaction

from apps.authentication.exceptions import UserExistException
from apps.authentication.models import Address, RegistrationToken, User
from apps.authentication.selectors import UserSelector
from apps.celery.utils import celery_apply_async
from apps.email.consts import EmailType
from apps.email.tasks import send_email_async
from config import settings


class AuthenticationServices:
    @staticmethod
    def create_user(user_data: dict) -> User:
        # function assert serialized data, but add one more secure
        email = user_data.pop("email")
        language = user_data.pop("language")
        password = user_data.pop("password")

        if UserSelector.get_by_username_or_none(email):
            raise UserExistException

        token = None

        with transaction.atomic():
            user = User.objects.create(username=email, defaults={"email": email, "language": language})
            user.set_password(password)
            user.save()
            token = RegistrationToken.objects.create(user=user)
        celery_apply_async(
            send_email_async,
            args=[
                EmailType.USER_REGISTER_EMAIL.value,
                [user.email],
                {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "domain": settings.DOMAIN,
                    "token_id": token.id,
                    "user_id": user.id,
                },
            ],
            countdown=30,
        )

        return user


class AddressServices:
    @staticmethod
    def create_address(address_data: dict) -> Address:
        # TODO: Add validators for creating address
        address = Address.objects.create(
            address_line_1=address_data["address_line_1"],
            address_line_2=address_data["address_line_2"],
            post_code=address_data["post_code"],
            city=address_data["city"],
            country=address_data["country"],
        )
        return address

    @staticmethod
    def update_address(address_data: dict) -> Address:
        address, _ = Address.objects.update_or_create(
            id=address_data["id"],
            defaults={
                "address_line_1": address_data["address_line_1"],
                "address_line_2": address_data["address_line_2"],
                "post_code": address_data["post_code"],
                "city": address_data["city"],
                "country": address_data["country"],
            },
        )
        return address
