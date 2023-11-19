from rest_framework import serializers

from apps.dashboard.models import Dashboard
from apps.particular_task.serializers import TaskShortDetailsSerializer


class NewDashboardSerializer(serializers.ModelSerializer):
    project_id = serializers.UUIDField(required=True, allow_null=False)

    class Meta:
        model = Dashboard
        fields = (
            "project_id",
            "name",
            "description",
        )


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = (
            "id",
            "name",
            "description",
        )


class DashboardWithTasksSerializer(DashboardSerializer):
    task = TaskShortDetailsSerializer(many=True)
    project_name = serializers.SerializerMethodField()

    def get_project_name(self, obj):
        return obj.project.name

    class Meta(DashboardSerializer.Meta):
        fields = DashboardSerializer.Meta.fields + (
            "project_name",
            "task",
        )
