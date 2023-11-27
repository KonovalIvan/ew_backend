from django.urls import path

from apps.api.images.view import ImageAssetView, NewImageView

urlpatterns = [
    path("<uuid:image_id>/", ImageAssetView.as_view(), name="images"),
    path("add/", NewImageView.as_view(), name="images"),
]
