from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.base_auth import TokenAuth
from apps.comments.serializers import CommentsSerializer, NewCommentSerializer
from apps.comments.services import CommentsServices


class AddCommentView(TokenAuth, APIView):
    serializer_class = NewCommentSerializer
    response_serializer = CommentsSerializer

    @extend_schema(
        responses={status.HTTP_200_OK: CommentsSerializer},
    )
    def post(self, request: Request) -> Response:
        """Create new Comments"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = CommentsServices.add_comment(serializer.validated_data, request.user)
        return Response(self.response_serializer(response).data, status=status.HTTP_201_CREATED)
