from typing import Any

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.base_auth import NoAuth, TokenAuth
from apps.authentication.selectors import UserSelector
from apps.authentication.serializers import (
    LoginSerializer,
    RegisterUserSerializer,
    TokenSerializer,
    UserDetailsSerializer,
)
from apps.authentication.services import AuthenticationServices


class LoginView(NoAuth, APIView):
    serializer_class = LoginSerializer

    @extend_schema(
        responses={status.HTTP_200_OK: TokenSerializer},
    )
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        if not (
            user := UserSelector.get_by_username_or_none(
                username=serializer.validated_data["username"],
            )
        ) or not user.check_password(serializer.validated_data["password"]):
            return Response({"error_msg": "Invalid username or password."}, status=status.HTTP_400_BAD_REQUEST)
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "access_token": token.key,
                "refresh_token": user.auth_token.key,
            }
        )


class VerifyTokenView(TokenAuth, APIView):
    """
    View for the first shot after firing up the application. If token doesn't walid user must login
    """

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return Response({"message": "Token is valid"}, status=status.HTTP_200_OK)


class UserDetailsView(TokenAuth, APIView):
    serializer_class = UserDetailsSerializer

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Get user info"""
        user = request.user
        serializer = self.serializer_class(user, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # ---------------------------------------NOT USED YET-------------------------------------------------------------

    def delete(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Delete user"""
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            # TODO: Add service for deleting user
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Change user"""
        serializer = self.serializer_class(request.user, many=False)
        serializer.is_valid()
        # TODO: Create service for change user by data from response

        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterUserView(NoAuth, APIView):
    serializer_class = RegisterUserSerializer

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Create new user"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.validated_data
        AuthenticationServices.create_user(user_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
