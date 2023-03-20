from rest_framework import serializers

from apps.projects.models import BuildingProject


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingProject
        fields = "__all__"
