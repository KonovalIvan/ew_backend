from typing import Any
from uuid import UUID

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.base_auth import TokenAuth
from apps.particular_task.selectors import TaskSelector
from apps.particular_task.serializers import (
    NewTaskSerializer,
    TaskSerializer,
    TaskShortDetailsSerializer,
)
from apps.particular_task.services import TaskServices


class NewTaskView(TokenAuth, APIView):
    serializer_class = NewTaskSerializer
    response_serializer = TaskShortDetailsSerializer

    @extend_schema(
        responses={status.HTTP_200_OK: NewTaskSerializer},
    )
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = TaskServices.create_task(data=serializer.validated_data, creator=request.user)
        return Response(self.response_serializer(response).data, status=status.HTTP_201_CREATED)


class SingleTaskView(TokenAuth, GenericAPIView):
    serializer_class = TaskSerializer
    update_serializer = NewTaskSerializer

    @extend_schema(
        responses={status.HTTP_200_OK: TaskSerializer},
    )
    def get(self, request: Request, task_id: UUID) -> Response:
        """Get task by ID"""
        tasks = TaskSelector.get_by_id(id=task_id)

        return Response(self.serializer_class(tasks, many=False).data, status=status.HTTP_200_OK)

    def delete(self, request: Request, task_id: UUID) -> Response:
        """Delete task by ID"""
        success = TaskServices.delete_task_by_id(task_id=task_id)

        return (
            Response(status=status.HTTP_204_NO_CONTENT)
            if success
            else Response({"error_msg": "Failed to find a dashboard."}, status=status.HTTP_404_NOT_FOUND)
        )

    def put(self, request: Request, task_id: UUID) -> Response:
        """Edit project by ID"""
        serializer = self.update_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = TaskServices.update_task(data=serializer.validated_data, task_id=task_id)
        return Response(self.get_serializer(response).data, status=status.HTTP_200_OK)
