from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import ProgressRecord
from .serializers import ProgressRecordSerializer
from apps.child_profiles.models import ChildProfile


class ChildProgressListView(generics.ListAPIView):
    """
    List learning progress records for a specific child.
    Enforces object-level ownership: only the guardian of this child can view progress.
    """
    serializer_class = ProgressRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        child_id = self.kwargs.get('child_id')
        child = get_object_or_404(ChildProfile, id=child_id, is_active=True)

        if child.guardian != self.request.user:
            return ProgressRecord.objects.none()

        return ProgressRecord.objects.filter(child_profile=child).select_related('game', 'game__category')

    def list(self, request, *args, **kwargs):
        child_id = self.kwargs.get('child_id')
        child = get_object_or_404(ChildProfile, id=child_id, is_active=True)

        if child.guardian != request.user:
            return Response(
                {"error": {"code": "FORBIDDEN", "message": "Ushbu bola profili ma’lumotlariga kirish taqiqlangan."}},
                status=status.HTTP_403_FORBIDDEN
            )

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "child_id": str(child.id),
            "display_name": child.display_name,
            "age_band": child.age_band,
            "total_games_played": queryset.count(),
            "records": serializer.data
        })
