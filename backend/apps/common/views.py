from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.db import connection
from drf_spectacular.utils import extend_schema, OpenApiResponse


class HealthCheckView(APIView):
    """
    General health check endpoint for Bolajon backend.
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


class LivenessHealthCheckView(APIView):
    """
    BJ-125: Liveness probe for Kubernetes/Docker container monitoring.
    Returns 200 immediately if python worker process is responding.
    Does NOT query DB to prevent cascading failures during DB strain.
    """
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Liveness Check",
        description="Quick liveness probe to verify container process is alive.",
        responses={200: OpenApiResponse(description="Process is alive")}
    )
    def get(self, request):
        return Response({
            "status": "alive",
            "service": "bolajon-api"
        }, status=status.HTTP_200_OK)


class ReadinessHealthCheckView(APIView):
    """
    BJ-125: Readiness probe for load balancers.
    Checks DB connectivity. Returns 503 if DB is not ready so ingress does not route user traffic.
    """
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Readiness Check",
        description="Readiness probe verifying DB connectivity before serving traffic.",
        responses={
            200: OpenApiResponse(description="Service is ready for traffic"),
            503: OpenApiResponse(description="Dependencies not ready")
        }
    )
    def get(self, request):
        db_ready = True
        cache_ready = True

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
        except Exception:
            db_ready = False

        from django.core.cache import cache
        try:
            cache.set("bolajon:readiness_probe", "1", timeout=5)
            cache_ready = cache.get("bolajon:readiness_probe") == "1"
        except Exception:
            cache_ready = False

        is_ready = db_ready  # DB is critical requirement for readiness

        return Response({
            "status": "ready" if is_ready else "not_ready",
            "database": "connected" if db_ready else "disconnected",
            "cache": "connected" if cache_ready else "degraded"
        }, status=status.HTTP_200_OK if is_ready else status.HTTP_503_SERVICE_UNAVAILABLE)
