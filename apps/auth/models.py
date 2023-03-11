from typing import Any

from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models

from apps.auth.consts import UserType
from apps.base_models import BaseModel, TimestampMixin


class Address(BaseModel):
    address_line_1 = models.CharField(max_length=128, blank=True, null=True)
    address_line_2 = models.CharField(max_length=128, blank=True, null=True)
    post_code = models.CharField(max_length=32, blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    country = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        verbose_name_plural = "addresses"

    def __str__(self) -> str:
        parts_to_display = [self.address_line_1, self.address_line_2, self.post_code, self.city, self.country]
        return ", ".join([str(parts) for parts in parts_to_display if str(parts) != ""])


class User(AbstractUser, BaseModel):
    REQUIRED_FIELDS = ["email", "username"]
    USERNAME_FIELD = "username"

    company_name = models.CharField(max_length=128)
    user_type = models.CharField(max_length=128, default=UserType.CLIENT, choices=UserType.choice(), blank=False, null=False)


    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} / {self.email}"
