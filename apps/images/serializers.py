from rest_framework import serializers

from apps.images.models import ImageAsset


class ImageAssetShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageAsset
        fields = (
            "id",
            "image",
            "image_name",
            "image_size",
        )


class NewImageSerializer(serializers.ModelSerializer):
    project_id = serializers.UUIDField(required=True)

    class Meta:
        model = ImageAsset
        fields = (
            "image",
            "project_id",
            "image_name",
        )
