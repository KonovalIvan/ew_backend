from typing import Any

from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.api.base_auth import NoAuth, TokenAuth
from apps.authentication.serializers import (
    BeaverSerializer,
    LoginSerializer,
    UserSerializer,
)


class UserApiView(TokenAuth):
    serializer_class = UserSerializer

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Get all users"""
        user = request.user
        serializer = self.serializer_class(user, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Create new user"""
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(NoAuth):
    serializer_class = LoginSerializer

    @extend_schema(
        responses={status.HTTP_200_OK: BeaverSerializer},
    )
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"error": "Invalid Credentials"}, status=400)
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }
        )
