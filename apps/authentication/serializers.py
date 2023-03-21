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


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
        )


class UserShortDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )


class UserDetailsSerializer(UserShortDetailsSerializer):
    address = AddressSerializer()

    class Meta:
        model = User
        fields = UserShortDetailsSerializer.Meta.fields + (
            "first_name",
            "last_name",
            "user_type",
            "user_type",
            "language",
            "address",
        )


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "password"]


class BeaverSerializer(serializers.ModelSerializer):
    access = serializers.CharField(required=True)
    refresh = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["access", "refresh"]
