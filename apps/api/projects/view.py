from typing import Any
from uuid import UUID

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.base_auth import TokenAuth
from apps.api.projects.serializers import ProjectsShortInfoQuerySerializer
from apps.projects.selectors import ProjectSelector
from apps.projects.serializers import (
    ActiveProjectsAndTasksSerializer,
    NewProjectsSerializer,
    ProjectsSerializer,
    ProjectsShortInfoSerializer,
)
from apps.projects.services import ProjectsServices


class ActiveProjectsAndTasksView(TokenAuth, APIView):
    serializer_class = ActiveProjectsAndTasksSerializer

    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Get count of active projects and active tasks"""
        user = request.user
        active_projects, active_tasks = ProjectsServices.get_count_of_active_projects_and_tasks(user=user)
        data_to_serialize = {"active_projects": active_projects, "active_tasks": active_tasks}
        serializer = self.serializer_class(data=data_to_serialize)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectsShortInfoView(TokenAuth, APIView):
    serializer_class = ProjectsShortInfoSerializer

    @extend_schema(
        responses={status.HTTP_200_OK: serializer_class},
        parameters=[
            OpenApiParameter(
                "is_archived",
                OpenApiTypes.BOOL,
                description="If True - method will send request to second database with archived projects",
                default=False,
            )
        ],
    )
    def get(self, request: Request) -> Response:
        """Get all projects and return short info, name image and description"""
        query_params = ProjectsShortInfoQuerySerializer(data=request.query_params)
        query_params.is_valid(raise_exception=True)

        projects = ProjectSelector.get_all_by_user(
            user=request.user, is_archived=query_params.validated_data["is_archived"]
        )
        projects.order_by("-created_at")

        return Response(self.serializer_class(projects, many=True).data, status=status.HTTP_200_OK)


class AddProjectView(TokenAuth, APIView):
    serializer_class = NewProjectsSerializer
    response_serializer = ProjectsSerializer

    @swagger_auto_schema(
        request_body=NewProjectsSerializer,
        responses={
            status.HTTP_201_CREATED: serializer_class,
            status.HTTP_400_BAD_REQUEST: "Bad request data.",
        },
    )
    def post(self, request: Request):
        """Create new project"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = ProjectsServices.create_project(serializer.validated_data)
        return Response(self.response_serializer(response).data, status=status.HTTP_201_CREATED)


class SingleProjectView(TokenAuth, GenericAPIView):
    serializer_class = ProjectsSerializer
    update_serializer = NewProjectsSerializer

    def get(self, request: Request, project_id: UUID) -> Response:
        """Get expanded project information by ID"""
        project = ProjectSelector.get_by_id(id=project_id)
        serializer = self.serializer_class(project, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, project_id: UUID) -> Response:
        """Delete project by ID"""
        success = ProjectsServices.delete_single_project_by_id(project_id=project_id)

        return (
            Response(status=status.HTTP_204_NO_CONTENT)
            if success
            else Response({"error_msg": "Failed to find a project."}, status=status.HTTP_404_NOT_FOUND)
        )

    def put(self, request: Request, project_id: UUID) -> Response:
        """Edit project by ID"""
        serializer = self.update_serializer(data=request.data)
        # TODO: Validator for length project name
        serializer.is_valid(raise_exception=True)

        response = ProjectsServices.update_project(data=serializer.validated_data, project_id=project_id)
        return Response(self.serializer_class(response).data, status=status.HTTP_200_OK)
