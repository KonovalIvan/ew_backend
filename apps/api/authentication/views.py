from typing import Any

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from apps.api.base_auth import NoAuth, TokenAuth
from apps.authentication.serializers import (
    BeaverSerializer,
    LoginSerializer,
    RegisterUserSerializer,
    UserDetailsSerializer,
)


class UserDetailsView(TokenAuth):
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


class RegisterUserView(TokenAuth):
    serializer_class = RegisterUserSerializer

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Create new user"""
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(NoAuth):
    serializer_class = LoginSerializer

    @extend_schema(
        responses={status.HTTP_200_OK: BeaverSerializer},
    )
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        # username = request.data.get("username")
        # password = request.data.get("password")
        return Response({"soon"})
