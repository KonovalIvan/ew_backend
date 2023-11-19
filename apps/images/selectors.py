from uuid import UUID

from apps.images.models import ImageAsset


class ImageAssetSelector:
    @staticmethod
    def get_by_id(id: UUID) -> ImageAsset:
        return ImageAsset.objects.get(id=id)
