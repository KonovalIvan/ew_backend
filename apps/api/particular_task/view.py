from uuid import UUID

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.base_auth import TokenAuth
from apps.dashboard.selectors import DashboardSelector
from apps.particular_task.selectors import TaskSelector
from apps.particular_task.serializers import TaskSerializer

# ---------------------------------------NOT USED YET-------------------------------------------------------------


class TaskView(TokenAuth, APIView):
    serializer_class = TaskSerializer

    # def get(self, request: Request, dashboard_id: UUID) -> Response:
    #     """Get all tasks for dashboard"""
    #     dashboard = DashboardSelector.get_by_id(id=dashboard_id)
    #     tasks = TaskSelector.get_all_by_dashboard(dashboard=dashboard)
    #
    #     return Response(self.serializer_class(tasks).data, status=status.HTTP_200_OK)

    def post(self, request: Request, dashboard_id: UUID) -> Response:
        """Create new task for dashboard"""
        dashboard = DashboardSelector.get_by_id(id=dashboard_id)
        serializer = self.serializer_class(request.data)
        serializer.is_valid(raise_exception=True)

        # TODO: Create logic for create new task

        return Response(self.serializer_class(dashboard).data, status=status.HTTP_200_OK)


class SingleTaskView(TokenAuth, APIView):
    serializer_class = TaskSerializer

    def get(self, request: Request, task_id: UUID) -> Response:
        """Get task by ID"""
        tasks = TaskSelector.get_by_id(id=task_id)

        return Response(self.serializer_class(tasks, many=False).data, status=status.HTTP_200_OK)

    def put(self, request: Request, task_id: UUID) -> Response:
        """Edit dashboard by ID"""
        tasks = TaskSelector.get_by_id(id=task_id)
        serializer = self.serializer_class(request.data, many=True)
        serializer.is_valid()

        # TODO: create edit logic in services

        return Response(self.serializer_class(tasks).data, status=status.HTTP_200_OK)

    def delete(self, request: Request, task_id: UUID) -> Response:
        """Delete dashboard by ID"""
        tasks = TaskSelector.get_by_id(id=task_id)
        serializer = self.serializer_class(request.data, many=True)
        serializer.is_valid()

        # TODO: create delete logic in services

        return Response(self.serializer_class(tasks).data, status=status.HTTP_200_OK)
