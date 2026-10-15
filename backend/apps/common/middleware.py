import uuid
import time
import logging

logger = logging.getLogger('bolajon.request')


class RequestIDMiddleware:
    """
    Attaches a unique correlation ID (X-Request-ID) to every HTTP request and response.
    Provides structured, safe telemetry without logging child PII or credentials.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_id = request.headers.get('X-Request-ID', str(uuid.uuid4()))
        request.request_id = request_id

        start_time = time.time()
        response = self.get_response(request)
        duration_ms = round((time.time() - start_time) * 1000, 2)

        response['X-Request-ID'] = request_id

        # Safe structured logging: path, status, duration. No passwords, tokens, or child PII.
        logger.info(
            f"request_id={request_id} method={request.method} path={request.path} "
            f"status={response.status_code} duration_ms={duration_ms}"
        )

        return response
