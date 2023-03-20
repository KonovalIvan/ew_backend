from typing import Any

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from apps.api.base_auth import TokenAuth
from apps.projects.selectors import ProjectSelector
from apps.projects.serializers import ProjectsSerializer


class ProjectApiView(TokenAuth):
    serializer_class = ProjectsSerializer

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Get all users"""
        user = request.user
        projects = ProjectSelector.get_all_by_owner(owner=user)
        serializer = self.serializer_class(projects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
