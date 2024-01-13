from typing import Any

from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.base_auth import NoAuth, TokenAuth
from apps.authentication.selectors import UserSelector
from apps.authentication.serializers import (
    ConfirmEmailSerializer,
    LoginSerializer,
    TokenSerializer,
    UserDetailsSerializer,
)


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


class ConfirmEmailView(NoAuth, APIView):
    serializer_class = ConfirmEmailSerializer

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # token_id = request.GET.get("token_id", None)
        # user_id = request.GET.get("user_id", None)
        data = {"is_email_confirmed": False, "additional_information": "lalalallalalala"}

        return render(request, template_name="confirm_email_view.html", context=data)
