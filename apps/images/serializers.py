from rest_framework import serializers

from apps.images.models import ImageAsset


class ImageAssetShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageAsset
        fields = (
            "id",
            "image",
        )
