from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.authtoken.models import Token


class BearerAuthentication(TokenAuthentication):
    keyword = "Bearer"

    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed("Invalid token")

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed("User inactive or deleted")

        return (token.user, token)

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1 or len(auth) > 2:
            raise exceptions.AuthenticationFailed("Invalid token header.")

        try:
            token = auth[1].decode()
        except UnicodeError:
            raise exceptions.AuthenticationFailed(
                "Invalid token header. Token string should not contain invalid characters."
            )

        return self.authenticate_credentials(token)

    def authenticate_header(self, request):
        return self.keyword
