from django.contrib import admin

from apps.images.models import ImageAsset


class ImageAssetInline(admin.TabularInline):
    model = ImageAsset
    extra = 0


admin.site.register(ImageAsset)
