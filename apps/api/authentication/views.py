from typing import Any

from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.authentication.models import User
from apps.authentication.serializers import UserSerializer
from swagger.schemas import LoginApiViewSchema, UserApiViewSchema


class UserApiView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Get all users"""
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=UserApiViewSchema.request_body_schema(),
        responses=UserApiViewSchema.response_schema(),
    )
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Create new user"""
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(APIView):
    @swagger_auto_schema(
        request_body=LoginApiViewSchema.request_body_schema(),
        responses=LoginApiViewSchema.response_schema(),
    )
    def post(self, request, username, password, *args, **kwargs):
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"error": "Invalid Credentials"}, status=400)
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh),
            }
        )
