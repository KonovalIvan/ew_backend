from typing import Any

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.base_consts import bytes_kb, bytes_mb
from apps.images.models import ImageAsset


@receiver(post_save, sender=ImageAsset)
def add_user_to_comment(sender: ImageAsset, instance: ImageAsset, *args: Any, **kwargs: Any) -> None:
    byte_size = instance.get_image_size()
    new_image_size = (
        f"{byte_size * bytes_mb:.2f} MB" if int(byte_size * bytes_mb) != 0 else f"{byte_size * bytes_kb:.2f} KB"
    )
    if instance.image_size != new_image_size:
        instance.image_size = new_image_size
        instance.save()
