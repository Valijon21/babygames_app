from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.db import connection
from drf_spectacular.utils import extend_schema, OpenApiResponse


class HealthCheckView(APIView):
    """
    Liveness and readiness health check endpoint for Bolajon backend.
    Returns status 200 when database connectivity is functional, 503 if impaired.
    """
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Health Check",
        description="Checks service health and database connectivity.",
        responses={
            200: OpenApiResponse(description="Service is healthy"),
            503: OpenApiResponse(description="Service dependency is unhealthy")
        }
    )
    def get(self, request):
        db_status = "ok"
        http_status = status.HTTP_200_OK

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
        except Exception:
            db_status = "unhealthy"
            http_status = status.HTTP_503_SERVICE_UNAVAILABLE

        return Response({
            "status": "healthy" if db_status == "ok" else "degraded",
            "service": "bolajon-api",
            "database": db_status
        }, status=http_status)
