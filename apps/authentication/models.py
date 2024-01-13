from django.contrib.auth.models import AbstractUser, Group, Permission
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
    company_name = models.CharField(max_length=128)
    user_type = models.CharField(
        max_length=128,
        default=UserType.CLIENT,
        choices=UserType.choice(),
        blank=False,
        null=False,
    )
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    language = models.CharField(
        max_length=2,
        default=Language(DEFAULT_USER_LANGUAGE).value,
        choices=Language.choice(),
        blank=False,
        null=False,
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to.",
        related_name="custom_user_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="custom_user_set",
        related_query_name="user",
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} / {self.email}"
