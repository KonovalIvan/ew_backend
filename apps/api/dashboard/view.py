from uuid import UUID

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.base_auth import TokenAuth
from apps.dashboard.selectors import DashboardSelector
from apps.dashboard.serializers import DashboardSerializer
from apps.projects.selectors import ProjectSelector

# ---------------------------------------NOT USED YET-------------------------------------------------------------


class DashboardsView(TokenAuth, APIView):
    serializer_class = DashboardSerializer

    def get(self, request: Request, project_id: UUID) -> Response:
        """Get dashboards by project"""
        project = ProjectSelector.get_by_id(id=project_id)
        dashboards = DashboardSelector.get_all_by_project(project=project)

        return Response(self.serializer_class(dashboards, many=True).data, status=status.HTTP_200_OK)


class SingleDashboardsView(TokenAuth, APIView):
    serializer_class = DashboardSerializer

    def get(self, request: Request, dashboard_id: UUID) -> Response:
        """Get dashboard by ID"""
        dashboard = DashboardSelector.get_by_id(id=dashboard_id)

        return Response(self.serializer_class(dashboard).data, status=status.HTTP_200_OK)

    def put(self, request: Request, project_id: UUID) -> Response:
        """Edit dashboard by ID"""
        dashboard = ProjectSelector.get_by_id(id=project_id)
        serializer = self.serializer_class(request.data, many=True)
        serializer.is_valid()

        # TODO: create edit logic in services

        return Response(self.serializer_class(dashboard).data, status=status.HTTP_200_OK)

    def delete(self, request: Request, project_id: UUID) -> Response:
        """Delete dashboard by ID"""
        dashboard = ProjectSelector.get_by_id(id=project_id)
        serializer = self.serializer_class(request.data, many=True)
        serializer.is_valid()

        # TODO: create delete logic in services

        return Response(self.serializer_class(dashboard).data, status=status.HTTP_200_OK)
