from rest_framework import serializers

from apps.dashboard.models import Dashboard


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = (
            "id",
            "name",
            "description",
        )
