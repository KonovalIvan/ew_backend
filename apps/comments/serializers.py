from rest_framework import serializers

from apps.comments.models import Comments


class NewCommentSerializer(serializers.ModelSerializer):
    task_id = serializers.UUIDField(required=False, allow_null=True)
    comments_id = serializers.UUIDField(required=False, allow_null=True)

    class Meta:
        model = Comments
        fields = (
            "description",
            "task_id",
            "comments_id",
        )

    def validate(self, data):
        if (not data.get("task_id") and not data.get("comments_id")) or (
            data.get("task_id") and data.get("comments_id")
        ):
            raise serializers.ValidationError("Either task_id or comment_id is required.")

        return data


class CommentsSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    creator_avatar = serializers.ImageField(source="creator.avatar", read_only=True)
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = (
            "id",
            "updated_at",
            "description",
            "task_id",
            "replies",
            "creator_avatar",
        )

    def get_updated_at(self, instance):
        return instance.updated_at.strftime("%d.%m.%Y")

    def get_replies(self, obj):
        replies = obj.replies.all()
        serialized_replies = self.recursive_serialize(replies)
        return serialized_replies

    def recursive_serialize(self, replies):
        serialized_data = []
        for reply in replies:
            data = {
                "id": reply.id,
                "updated_at": reply.updated_at.strftime("%d.%m.%Y"),
                "description": reply.description,
                "task_id": reply.task_id,
                "creator_avatar": reply.creator.avatar.url if reply.creator else None,
                "replies": self.recursive_serialize(reply.replies.all()),
            }
            serialized_data.append(data)
        return serialized_data
