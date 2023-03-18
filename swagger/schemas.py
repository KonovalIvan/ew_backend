from drf_yasg import openapi

from apps.authentication.serializers import UserSerializer


# TODO: create advanced schema, extands and others.
class UserApiViewSchema:
    @staticmethod
    def request_body_schema():
        return openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )

    @staticmethod
    def response_schema():
        return {200: openapi.Response(description="", schema=UserSerializer)}


class LoginApiViewSchema:
    @staticmethod
    def request_body_schema():
        return openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )

    @staticmethod
    def response_schema():
        return {
            200: openapi.Response(
                description="",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={"access": openapi.Schema(type=openapi.TYPE_STRING)},
                ),
            )
        }
