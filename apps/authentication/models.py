from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.authentication.consts import DEFAULT_USER_LANGUAGE, Language, UserType
from apps.base_models import BaseModel, TimestampMixin
from apps.base_services import generate_random_filename_for_user_avatar


class Address(BaseModel, TimestampMixin):
    """
    That model serve for addresses
    """

    address_line_1 = models.CharField(
        max_length=128,
    )
    address_line_2 = models.CharField(
        max_length=128,
        blank=True,
        null=True,
    )
    post_code = models.CharField(
        max_length=32,
    )
    city = models.CharField(
        max_length=256,
    )
    country = models.CharField(
        max_length=256,
    )

    class Meta:
        verbose_name_plural = "addresses"

    def __str__(self) -> str:
        parts_to_display = [
            self.address_line_1,
            self.address_line_2,
            self.post_code,
            self.city,
            self.country,
        ]
        return ", ".join([str(parts) for parts in parts_to_display if str(parts) != ""])


class User(AbstractUser, BaseModel, TimestampMixin):
    """
    This model created for the user
    """

    avatar = models.ImageField(
        upload_to=generate_random_filename_for_user_avatar,
        null=True,
        blank=True,
    )
    user_type = models.CharField(
        max_length=128,
        default=UserType.CLIENT,
        choices=UserType.choice(),
        blank=False,
        null=False,
    )
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    language = models.CharField(
        max_length=2,
        default=Language(DEFAULT_USER_LANGUAGE).value,
        choices=Language.choice(),
        blank=False,
        null=False,
    )
    is_registered = models.BooleanField(
        default=False, help_text="if true means that the user has completed the registration process"
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} / {self.email}"


class RegistrationToken(BaseModel, TimestampMixin):
    """
    This model created for the user
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    is_verify = models.BooleanField(default=False, help_text="if true - user open verify link, and finish registrarion")

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name} / {self.is_verify}"
