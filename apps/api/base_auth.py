from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class NoAuth:
    """All user can use endpoint"""

    permission_classes = ()
    authentication_classes = ()


class TokenAuth:
    """Ensures user is authenticated"""

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
