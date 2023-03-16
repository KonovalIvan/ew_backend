from rest_framework import serializers

from apps.authentication.models import Address, User


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ("address_line_1", "address_line_2", "post_code", "city", "country")
        extra_kwargs = {
            "address_line_1": {"required": True},
            "post_code": {"required": True},
            "city": {"required": True},
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "user_type")
