from apps.base_exceptions import BaseEwException


class ImageRelatedModelsEmptyException(BaseEwException):
    error_msg = "At least one of the related models is required"
    key = "empty-related-models-error"
