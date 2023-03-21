from rest_framework import serializers

from apps.authentication.serializers import (
    AddressSerializer,
    UserShortDetailsSerializer,
)
from apps.projects.models import BuildingProject


class ProjectsSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    client = UserShortDetailsSerializer()
    owner = UserShortDetailsSerializer()
    building_master = UserShortDetailsSerializer()
    designer = UserShortDetailsSerializer()

    class Meta:
        model = BuildingProject
        fields = "__all__"
