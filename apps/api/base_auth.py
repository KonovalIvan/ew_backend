from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class NoAuth(APIView):
    """All user can use endpoint"""

    permission_classes = ()
    authentication_classes = ()


class TokenAuth(APIView):
    """Ensures user is authenticated"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
