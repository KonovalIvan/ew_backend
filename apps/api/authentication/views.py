from typing import Any

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.base_auth import TokenAuth
from apps.authentication.models import User
from apps.authentication.selectors import UserSelector
from apps.authentication.serializers import (
    LoginSerializer,
    RegisterUserSerializer,
    TokenSerializer,
    UserDetailsSerializer,
)


class UserDetailsView(TokenAuth, APIView):
    serializer_class = UserDetailsSerializer

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Get user info"""
        user = request.user
        serializer = self.serializer_class(user, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

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


class RegisterUserView(TokenAuth, APIView):
    serializer_class = RegisterUserSerializer

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Create new user"""
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    serializer_class = LoginSerializer

    @extend_schema(
        responses={status.HTTP_200_OK: TokenSerializer},
    )
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.serializer_class(data=request.data, context={"request": request})
        if serializer.is_valid():
            try:
                user = UserSelector.get_by_username(
                    username=serializer.validated_data["username"],
                )
                if not user.check_password(serializer.validated_data["password"]):
                    raise User.DoesNotExist
            except User.DoesNotExist:
                return Response(
                    {"non_field_errors": ["Invalid username or password."]}, status=status.HTTP_400_BAD_REQUEST
                )
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                    "refresh_token": user.auth_token.key,
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
