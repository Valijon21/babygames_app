from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.utils import timezone
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from .models import GameSession
from .serializers import SessionStartSerializer, SessionCompleteSerializer, GameSessionSerializer
from apps.child_profiles.models import ChildProfile
from apps.progress.models import ProgressRecord


class SessionStartView(APIView):
    """Start an interactive game session."""
    permission_classes = [AllowAny]

    @extend_schema(request=SessionStartSerializer, responses={201: GameSessionSerializer})
    def post(self, request):
        serializer = SessionStartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        game = serializer.validated_data['game_slug']
        child_id = serializer.validated_data.get('child_profile_id')

        child_profile = None
        if child_id:
            try:
                child_profile = ChildProfile.objects.get(id=child_id, is_active=True)
                if request.user.is_authenticated and child_profile.guardian != request.user:
                    return Response(
                        {"error": {"code": "FORBIDDEN", "message": "Bola profiliga kirish ruxsati yo‘q."}},
                        status=status.HTTP_403_FORBIDDEN
                    )
            except ChildProfile.DoesNotExist:
                pass

        session = GameSession.objects.create(
            game=game,
            child_profile=child_profile,
            status='started',
            content_version=game.content_version
        )
        return Response(GameSessionSerializer(session).data, status=status.HTTP_201_CREATED)


class SessionCompleteView(APIView):
    """Submit gameplay results and record learning progress."""
    permission_classes = [AllowAny]

    @extend_schema(request=SessionCompleteSerializer, responses={200: dict})
    def post(self, request, pk):
        session = get_object_or_404(GameSession, pk=pk)

        if session.child_profile and request.user.is_authenticated:
            if session.child_profile.guardian != request.user:
                return Response(
                    {"error": {"code": "FORBIDDEN", "message": "Ushbu sessiyani yakunlash ruxsati yo‘q."}},
                    status=status.HTTP_403_FORBIDDEN
                )

        serializer = SessionCompleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        session.completed_at = timezone.now()
        session.duration_seconds = data['duration_seconds']
        session.score = data.get('score')
        session.status = 'completed' if data.get('completed', True) else 'abandoned'
        session.content_version = data.get('content_version', 1)

        result_summary = data.get('result_summary', {})
        result_summary['attempts'] = data.get('attempts', 1)
        session.result_summary = result_summary
        session.save()

        progress_updated = False
        if session.child_profile and session.status == 'completed':
            record, _ = ProgressRecord.objects.get_or_create(
                child_profile=session.child_profile,
                game=session.game,
                defaults={'completed_count': 0, 'best_score': session.score}
            )
            record.completed_count += 1
            if session.score is not None:
                if record.best_score is None or session.score > record.best_score:
                    record.best_score = session.score
            record.save()
            progress_updated = True

        return Response({
            "id": str(session.id),
            "status": session.status,
            "score": session.score,
            "progress_updated": progress_updated
        }, status=status.HTTP_200_OK)
