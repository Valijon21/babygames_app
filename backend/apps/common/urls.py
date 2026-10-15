from django.urls import path
from .views import HealthCheckView, LivenessHealthCheckView, ReadinessHealthCheckView

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='health-check'),
    path('health/live/', LivenessHealthCheckView.as_view(), name='health-liveness'),
    path('health/ready/', ReadinessHealthCheckView.as_view(), name='health-readiness'),
]
