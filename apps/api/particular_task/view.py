from typing import Any

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.base_auth import TokenAuth
from apps.particular_task.serializers import (
    NewTaskSerializer,
    TaskShortDetailsSerializer,
)


class NewTaskView(TokenAuth, APIView):
    serializer_class = NewTaskSerializer
    response_serializer = TaskShortDetailsSerializer

    @extend_schema(
        responses={status.HTTP_200_OK: NewTaskSerializer},
    )
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        from apps.particular_task.services import TaskServices

        response = TaskServices.create_task(serializer.validated_data)
        return Response(self.response_serializer(response).data, status=status.HTTP_201_CREATED)


# ---------------------------------------NOT USED YET-------------------------------------------------------------

# class SingleTaskView(TokenAuth, APIView):
#     serializer_class = TaskShortDetailsSerializer
#
#     def get(self, request: Request, task_id: UUID) -> Response:
#         """Get task by ID"""
#         tasks = TaskSelector.get_by_id(id=task_id)
#
#         return Response(self.serializer_class(tasks, many=False).data, status=status.HTTP_200_OK)
#
#     def put(self, request: Request, task_id: UUID) -> Response:
#         """Edit dashboard by ID"""
#         tasks = TaskSelector.get_by_id(id=task_id)
#         serializer = self.serializer_class(request.data, many=True)
#         serializer.is_valid()
#
#         # TODO: create edit logic in services
#
#         return Response(self.serializer_class(tasks).data, status=status.HTTP_200_OK)
#
#     def delete(self, request: Request, task_id: UUID) -> Response:
#         """Delete dashboard by ID"""
#         tasks = TaskSelector.get_by_id(id=task_id)
#         serializer = self.serializer_class(request.data, many=True)
#         serializer.is_valid()
#
#         # TODO: create delete logic in services
#
#         return Response(self.serializer_class(tasks).data, status=status.HTTP_200_OK)
