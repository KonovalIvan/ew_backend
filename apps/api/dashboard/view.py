from uuid import UUID

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.base_auth import TokenAuth
from apps.dashboard.selectors import DashboardSelector
from apps.dashboard.serializers import (
    DashboardSerializer,
    DashboardWithTasksSerializer,
    NewDashboardSerializer,
)
from apps.dashboard.services import DashboardServices


class AddDashboardsView(TokenAuth, APIView):
    serializer_class = NewDashboardSerializer
    response_serializer = DashboardSerializer

    def post(self, request: Request) -> Response:
        """Create new dashboard"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = DashboardServices.create_dashboard(serializer.validated_data)
        return Response(self.response_serializer(response).data, status=status.HTTP_201_CREATED)


class SingleDashboardsView(TokenAuth, GenericAPIView):
    serializer_class = DashboardWithTasksSerializer
    update_serializer = DashboardSerializer

    def get(self, request: Request, dashboard_id: UUID) -> Response:
        """Get dashboard and related tasks"""
        dashboard = DashboardSelector.get_by_id(id=dashboard_id)

        return Response(self.serializer_class(dashboard).data, status=status.HTTP_200_OK)

    def put(self, request: Request, dashboard_id: UUID) -> Response:
        """Edit project by ID"""
        serializer = self.update_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = DashboardServices.update_dashboard(data=serializer.validated_data, dashboard_id=dashboard_id)
        return Response(self.get_serializer(response).data, status=status.HTTP_200_OK)

    def delete(self, request: Request, dashboard_id: UUID) -> Response:
        """Delete dashboard by ID"""
        success = DashboardServices.delete_single_dashboard_by_id(dashboard_id=dashboard_id)

        return (
            Response(status=status.HTTP_204_NO_CONTENT)
            if success
            else Response({"error_msg": "Failed to find a dashboard."}, status=status.HTTP_404_NOT_FOUND)
        )


# ---------------------------------------NOT USED YET-------------------------------------------------------------

# def get(self, request: Request, project_id: UUID) -> Response:
#     """Get dashboards by project"""
#     project = ProjectSelector.get_by_id(id=project_id)
#     dashboards = DashboardSelector.get_all_by_project(project=project)
#
#     return Response(self.serializer_class(dashboards, many=True).data, status=status.HTTP_200_OK)

#
# class SingleDashboardsView(TokenAuth, APIView):
#     serializer_class = DashboardSerializer
#
#     def get(self, request: Request, dashboard_id: UUID) -> Response:
#         """Get dashboard by ID"""
#         dashboard = DashboardSelector.get_by_id(id=dashboard_id)
#
#         return Response(self.serializer_class(dashboard).data, status=status.HTTP_200_OK)
#
#     def put(self, request: Request, project_id: UUID) -> Response:
#         """Edit dashboard by ID"""
#         dashboard = ProjectSelector.get_by_id(id=project_id)
#         serializer = self.serializer_class(request.data, many=True)
#         serializer.is_valid()
#
#         # TODO: create edit logic in services
#
#         return Response(self.serializer_class(dashboard).data, status=status.HTTP_200_OK)
#
#     def delete(self, request: Request, project_id: UUID) -> Response:
#         """Delete dashboard by ID"""
#         dashboard = ProjectSelector.get_by_id(id=project_id)
#         serializer = self.serializer_class(request.data, many=True)
#         serializer.is_valid()
#
#         # TODO: create delete logic in services
#
#         return Response(self.serializer_class(dashboard).data, status=status.HTTP_200_OK)
