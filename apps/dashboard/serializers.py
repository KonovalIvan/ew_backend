from rest_framework import serializers

from apps.dashboard.models import Dashboard


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
        )
