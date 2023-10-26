from rest_framework import serializers

from apps.authentication.serializers import AddressSerializer, UserDetailsSerializer
from apps.dashboard.serializers import DashboardSerializer
from apps.projects.models import Project, ProjectGallery


class ProjectsShortInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "main_image",
            "description",
            "finished",
        )


class ProjectGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectGallery
        fields = (
            "id",
            "image",
        )


class ProjectsSerializer(serializers.ModelSerializer):
    designer = UserDetailsSerializer()
    building_master = UserDetailsSerializer()
    client = serializers.CharField(help_text="Here we add phone number of client", max_length=20)
    address = AddressSerializer()
    dashboard = DashboardSerializer(many=True)
    project_gallery = ProjectGallerySerializer(many=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "designer",
            "building_master",
            "client",
            "address",
            "dashboard",
            "project_gallery",
            "finished",
        )


class ActiveProjectsAndTasksSerializer(serializers.Serializer):
    active_projects = serializers.IntegerField(help_text="Count all active projects")
    active_tasks = serializers.IntegerField(help_text="All project progress information")
