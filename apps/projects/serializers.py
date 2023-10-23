from rest_framework import serializers

from apps.authentication.serializers import (
    AddressSerializer,
    UserShortDetailsSerializer,
)
from apps.projects.models import Project


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


class ProjectsSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    client = UserShortDetailsSerializer()
    owner = UserShortDetailsSerializer()
    building_master = UserShortDetailsSerializer()
    designer = UserShortDetailsSerializer()

    class Meta:
        model = Project
        fields = "__all__"


class ActiveProjectsAndTasksSerializer(serializers.Serializer):
    active_projects = serializers.IntegerField(help_text="Count all active projects")
    active_tasks = serializers.IntegerField(help_text="All project progress information")
