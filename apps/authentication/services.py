from typing import Dict, Any
from uuid import UUID

from django.db import transaction

from apps.authentication.exceptions import UserExistException, UserNotFoundException, TokenNotFoundException
from apps.authentication.models import Address, RegistrationToken, User
from apps.authentication.selectors import UserSelector, RegistrationTokenSelector
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

        with transaction.atomic():
            user = User.objects.create(username=email, defaults={"email": email, "language": language}, is_active=False)
            user.set_password(password)
            user.save()
            token = RegistrationToken.objects.create(user=user)
        celery_apply_async(
            send_email_async,
            args=[
                EmailType.USER_REGISTER_EMAIL.value,
                [user.email],
                {
                    "email": user.email,
                    "domain": settings.DOMAIN,
                    "token_id": token.id,
                    "user_id": user.id,
                    "language": user.language,
                },
            ],
            countdown=30,
        )

        return user

    @staticmethod
    def confirm_email(token_id: UUID, user_id: UUID) -> dict[str, Any]:
        try:
            user = UserSelector.get_by_id(id=user_id)
            if (token := RegistrationTokenSelector.get_by_id_and_user(id=token_id, user=user)) and not token.is_verify:
                token.is_verify, user.is_registered, user.is_active = True, True, True
                token.save()
                user.save()

                return {
                    "is_email_confirmed": True,
                }
            else:
                return {
                    "is_email_confirmed": False,
                    "reason": "Token is already verified",
                }
        except User.DoesNotExist:
            ex = UserNotFoundException
            return {"is_email_confirmed": False, "reason": ex.error_msg, }

        except RegistrationToken.DoesNotExist:
            ex = TokenNotFoundException
            return {"is_email_confirmed": False, "reason": ex.error_msg, }


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
