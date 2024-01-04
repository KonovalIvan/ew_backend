from rest_framework import serializers

from apps.comments.serializers import CommentsSerializer
from apps.images.serializers import ImageAssetShortSerializer
from apps.particular_task.models import Task


class TaskShortDetailsSerializer(serializers.ModelSerializer):
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = (
            "id",
            "name",
            "updated_at",
            "finished",
        )

    def get_updated_at(self, instance):
        return instance.created_at.strftime("%H:%M")


class NewTaskSerializer(serializers.ModelSerializer):
    dashboard_id = serializers.UUIDField(required=False)

    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "dashboard_id",
        )


class TaskSerializer(TaskShortDetailsSerializer):
    image_gallery = ImageAssetShortSerializer(
        many=True,
        read_only=True,
    )
    comments = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    project_id = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = TaskShortDetailsSerializer.Meta.fields + (
            "description",
            "project_id",
            "image_gallery",
            "created_at",
            "comments",
        )

    def get_project_id(self, instance):
        return instance.dashboard.project.id

    def get_updated_at(self, instance):
        return instance.created_at.strftime("%H:%M")

    def get_created_at(self, instance):
        return instance.created_at.strftime("%d.%m.%Y")

    def get_comments(self, obj):
        comments = obj.comments.all()
        serialized_data = []

        for comment in comments:
            serialized_replies = CommentsSerializer(comment, many=False).data
            serialized_data.append(serialized_replies)

        return serialized_data
