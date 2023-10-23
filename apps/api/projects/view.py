from typing import Any
from uuid import UUID

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.base_auth import TokenAuth
from apps.projects.selectors import ProjectSelector
from apps.projects.serializers import ProjectsProgressSerializer, ProjectsSerializer
from apps.projects.services import ProjectsProgressServices


class ActiveProjectsAndTasksView(TokenAuth, APIView):
    serializer_class = ProjectsProgressSerializer

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Get count of active projects and active tasks"""
        user = request.user
        active_projects, active_tasks = ProjectsProgressServices.get_count_of_active_projects_and_tasks(user=user)
        data_to_serialize = {"active_projects": active_projects, "active_tasks": active_tasks}
        serializer = self.serializer_class(data=data_to_serialize)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# ---------------------------------------NOT USED YET-------------------------------------------------------------


class ActiveProjectView(TokenAuth, APIView):
    serializer_class = ProjectsSerializer

    def get(self, request: Request) -> Response:
        """Get all active projects"""
        projects = ProjectSelector.get_active_by_owner(owner=request.user)

        return Response(self.serializer_class(projects, many=True).data, status=status.HTTP_200_OK)

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Create new project"""
        serializer = self.serializer_class(request.data, many=False)

        # TODO: create logic for creating new project

        return Response(self.serializer_class(serializer).data, status=status.HTTP_200_OK)


class SingleProjectView(TokenAuth, APIView):
    serializer_class = ProjectsSerializer

    def get(self, request: Request, project_id: UUID) -> Response:
        """Get expanded project information by ID"""
        project = ProjectSelector.get_by_id(id=project_id)
        serializer = self.serializer_class(project, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, project_id: UUID) -> Response:
        """Edit project by ID"""
        projects = ProjectSelector.get_by_id(id=project_id)
        serializer = self.serializer_class(projects, many=True)
        serializer.is_valid()

        # TODO: create edit logic in services

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, project_id: UUID) -> Response:
        """Delete project by ID"""
        projects = ProjectSelector.get_by_id(id=project_id)
        serializer = self.serializer_class(projects, many=True)
        serializer.is_valid()

        # TODO: create delete logic in services

        return Response(serializer.data, status=status.HTTP_200_OK)


class FinishedProjectView(TokenAuth, APIView):
    serializer_class = ProjectsSerializer

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Get all archived projects"""
        projects = ProjectSelector.get_archived_by_owner(owner=request.user)
        serializer = self.serializer_class(projects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
