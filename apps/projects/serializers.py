from rest_framework import serializers

from apps.authentication.serializers import AddressSerializer, UserDetailsSerializer
from apps.dashboard.serializers import DashboardSerializer
from apps.images.serializers import ImageAssetShortSerializer
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
    designer = UserDetailsSerializer()
    building_master = UserDetailsSerializer()
    client = serializers.CharField(help_text="Here we add phone number of client", max_length=20)
    address = AddressSerializer()
    dashboard = DashboardSerializer(many=True)
    image_gallery = ImageAssetShortSerializer(many=True)

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
            "image_gallery",
            "finished",
        )


class NewProjectsSerializer(serializers.ModelSerializer):
    designer_email = serializers.CharField(help_text="Designer email", max_length=20, required=False, allow_blank=True)
    building_master_email = serializers.CharField(
        help_text="Building master email", max_length=20, required=False, allow_blank=True
    )
    client_phone = serializers.CharField(help_text="Client phone", max_length=20, required=False, allow_blank=True)
    address = AddressSerializer(required=False, allow_null=True)
    description = serializers.CharField(allow_blank=True)

    class Meta:
        model = Project
        fields = (
            "name",
            "designer_email",
            "building_master_email",
            "client_phone",
            "description",
            "address",
        )


class ActiveProjectsAndTasksSerializer(serializers.Serializer):
    active_projects = serializers.IntegerField(help_text="Count all active projects")
    active_tasks = serializers.IntegerField(help_text="All project progress information")
