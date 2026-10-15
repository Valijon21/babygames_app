from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import ChildProfile
from .serializers import ChildProfileSerializer
from .permissions import IsGuardianOfChild


class ChildProfileViewSet(viewsets.ModelViewSet):
    """
    CRUD ViewSet for managing Child Profiles under the authenticated Guardian.
    Complies with COPPA and GDPR-K child privacy standards:
    - Zero child PII collected (only pseudonym and age band).
    - Object-level ownership strictly enforced (IsGuardianOfChild).
    - Right to Access / Portability via /api/v1/children/{id}/export/.
    - Right to Erasure via DELETE /api/v1/children/{id}/?hard_delete=true.
    """
    serializer_class = ChildProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsGuardianOfChild]

    def get_queryset(self):
        # Automatically scopes queries to the currently authenticated guardian
        return ChildProfile.objects.filter(guardian=self.request.user, is_active=True)

    def perform_create(self, serializer):
        serializer.save(guardian=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        hard_delete = request.query_params.get('hard_delete', 'false').lower() == 'true'

        if hard_delete:
            # Permanent erasure (Right to Erasure / COPPA compliance)
            instance.delete()
            return Response(
                {
                    "message": (
                        "Bola profili va unga bog‘liq barcha ma’lumotlar "
                        "butunlay o‘chirildi (COPPA/GDPR tozalash)."
                    ),
                    "erased": True
                },
                status=status.HTTP_200_OK
            )
        else:
            # Soft-delete by default
            instance.is_active = False
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get'])
    def export(self, request, pk=None):
        """
        BJ-095: Full child profile data portability export (COPPA/GDPR-K).
        Exports child pseudonymous profile, all game sessions, and mastery progress.
        """
        instance = self.get_object()

        # Collect session history
        sessions_data = [
            {
                "session_id": str(s.id),
                "game_slug": s.game.slug,
                "game_title": s.game.title,
                "status": s.status,
                "started_at": s.started_at.isoformat() if s.started_at else None,
                "completed_at": s.completed_at.isoformat() if s.completed_at else None,
                "duration_seconds": s.duration_seconds,
                "score": s.score,
                "result_summary": s.result_summary
            }
            for s in instance.game_sessions.all()
        ]

        # Collect progress records
        progress_data = [
            {
                "game_slug": p.game.slug,
                "game_title": p.game.title,
                "completed_count": p.completed_count,
                "best_score": p.best_score,
                "last_played_at": p.last_played_at.isoformat() if p.last_played_at else None
            }
            for p in instance.progress_records.all()
        ]

        return Response({
            "export_timestamp": timezone.now().isoformat(),
            "compliance": "COPPA / GDPR-K Data Portability Export",
            "guardian": {
                "id": request.user.id,
                "username": request.user.username,
                "email": request.user.email
            },
            "child_profile": {
                "id": str(instance.id),
                "display_name": instance.display_name,
                "age_band": instance.age_band,
                "created_at": instance.created_at.isoformat()
            },
            "game_sessions_count": len(sessions_data),
            "game_sessions": sessions_data,
            "progress_records_count": len(progress_data),
            "progress_records": progress_data
        })
