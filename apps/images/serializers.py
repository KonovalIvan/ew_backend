from rest_framework import serializers

from apps.images.exceptions import ImageRelatedModelsEmptyException
from apps.images.models import ImageAsset


class ImageAssetShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageAsset
        fields = (
            "id",
            "image",
        )


class ImageSerializer(ImageAssetShortSerializer):
    class Meta:
        model = ImageAsset
        fields = ImageAssetShortSerializer.Meta.fields + (
            "image_name",
            "image_size",
        )


class NewImageSerializer(serializers.ModelSerializer):
    project_id = serializers.UUIDField(required=False)
    task_id = serializers.UUIDField(required=False)

    class Meta:
        model = ImageAsset
        fields = (
            "image",
            "project_id",
            "task_id",
            "image_name",
        )

    def validate(self, attrs):
        project_id = attrs.get("project_id")
        task_id = attrs.get("task_id")

        if not project_id and not task_id:
            raise ImageRelatedModelsEmptyException
        return attrs
