from rest_framework import serializers

from apps.authentication.models import Address, User


class AddressSerializer(serializers.ModelSerializer):
    address_line_2 = serializers.CharField(required=False, default="")
    id = serializers.UUIDField(required=False, allow_null=True)

    class Meta:
        model = Address
        fields = (
            "id",
            "address_line_1",
            "address_line_2",
            "post_code",
            "city",
            "country",
        )


class RegisterUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "confirm_password",
        )

    def validate(self, data):
        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError("Passwords are different.")
        return data


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("avatar",)


class UserShortDetailsSerializer(UserAvatarSerializer):
    class Meta:
        model = User
        fields = UserAvatarSerializer.Meta.fields + (
            "first_name",
            "last_name",
        )


class UserDetailsSerializer(UserShortDetailsSerializer):
    class Meta:
        model = User
        fields = UserShortDetailsSerializer.Meta.fields + (
            "username",
            "email",
        )


class UserMainDetailsSerializer(UserDetailsSerializer):
    active_projects = serializers.IntegerField(help_text="Count all active projects")
    progress = serializers.DecimalField(help_text="All project progress information", decimal_places=2, max_digits=1000)

    class Meta:
        model = User
        fields = UserDetailsSerializer.Meta.fields + (
            "active_projects",
            "progress",
        )


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "password"]


class TokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(required=True)
    refresh_token = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["token", "refresh_token"]
