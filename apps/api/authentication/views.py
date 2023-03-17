from typing import Any

from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.models import User
from apps.authentication.serializers import UserSerializer


class UserApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Get all users"""
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Create new user"""
        data = {
            "username": request.data.get("username"),
            "first_name": request.data.get("first_name"),
            "last_name": request.data.get("last_name"),
            "email": request.data.get("email"),
            "user_type": request.data.get("user_type"),
        }
        serializer = self.serializer_class(data=data, many=False)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
