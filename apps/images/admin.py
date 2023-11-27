from django.contrib import admin

from apps.images.models import ImageAsset


class ImageAssetInline(admin.TabularInline):
    model = ImageAsset
    extra = 0


class ImageAssetAdmin(admin.ModelAdmin):
    model = ImageAsset
    list_display = (
        "image_name",
        "project",
        "image_size",
    )
    readonly_fields = ("image_size",)
    search_fields = ("project__name",)


admin.site.register(ImageAsset, ImageAssetAdmin)
