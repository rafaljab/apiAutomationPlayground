import logging

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        logger.info(f"Deleting user {user.username} (ID: {user.pk})")
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
