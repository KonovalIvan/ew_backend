from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class NoAuth(APIView):
    """All user can use endpoint"""

    permission_classes = ()
    authentication_classes = ()


class TokenAuth(APIView):
    """Ensures user is authenticated"""

    permission_classes = [IsAuthenticated]
