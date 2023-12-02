from rest_framework import serializers

from apps.particular_task.models import Task


class TaskShortDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "name",
            "updated_at",
            "finished",
        )


class NewTaskSerializer(serializers.ModelSerializer):
    dashboard_id = serializers.UUIDField(required=False)

    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "dashboard_id",
        )


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "name",
            "description",
        )
