from rest_framework import serializers

from apps.particular_task.models import Task


class TaskShortDetailsSerializer(serializers.ModelSerializer):
    # updated_at = serializers.SerializerMethodField()
    # def get_updated_at(self, obj):
    #     update_date = obj.updated_at
    #     return update_date.strftime("%H:%M")

    class Meta:
        model = Task
        fields = (
            "name",
            "updated_at",
            "finished",
        )
