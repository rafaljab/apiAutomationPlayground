import logging
from django.middleware.csrf import get_token

logger = logging.getLogger(__name__)


class CsrfTokenResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        try:
            token = get_token(request)
            if token:
                response["X-CSRFToken"] = token
        except Exception as e:
            logger.error(f"Error getting CSRF token: {e}")
        return response
