from django.urls import path

from apps.api.images.view import ImageAssetView

urlpatterns = [
    path("<uuid:image_id>/", ImageAssetView.as_view(), name="images"),
]
