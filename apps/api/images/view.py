from typing import Any
from uuid import UUID

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.base_auth import TokenAuth
from apps.images.services import ImageAssetServices


class ImageAssetView(TokenAuth, APIView):
    def delete(self, request: Request, image_id: UUID, *args: Any, **kwargs: Any) -> Response:
        """Delete image from db by id"""
        success = ImageAssetServices.remove_single_image_by_id(image_id=image_id)
        return (
            Response(status=status.HTTP_204_NO_CONTENT)
            if success
            else Response({"error_msg": "Failed to find photo."}, status=status.HTTP_404_NOT_FOUND)
        )
