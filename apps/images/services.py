from uuid import UUID

from apps.images.models import ImageAsset
from apps.images.selectors import ImageAssetSelector


class ImageAssetServices:
    @staticmethod
    def remove_single_image_by_id(image_id: UUID) -> bool:
        try:
            image = ImageAssetSelector.get_by_id(id=image_id)
            image.delete()
            return True
        except ImageAsset.DoesNotExist:
            # TODO: Add log for this exception
            return False
