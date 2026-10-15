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


class ChildProgressSummaryView(generics.RetrieveAPIView):
    """
    BJ-085: Aggregated learning progress summary for parent dashboard.
    Computes total stars, completed sessions, time spent, and per-category breakdown.
    Strictly restricted to the child's guardian.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, child_id, *args, **kwargs):
        child = get_object_or_404(ChildProfile, id=child_id, is_active=True)

        if child.guardian != request.user:
            return Response(
                {"error": {"code": "FORBIDDEN", "message": "Ushbu bola profili statistikasiga kirish taqiqlangan."}},
                status=status.HTTP_403_FORBIDDEN
            )

        from django.db.models import Sum

        progress_records = ProgressRecord.objects.filter(child_profile=child).select_related('game', 'game__category')

        total_games_played = progress_records.aggregate(total=Sum('completed_count'))['total'] or 0
        total_stars = progress_records.aggregate(total=Sum('best_score'))['total'] or 0

        completed_sessions = child.game_sessions.filter(status='completed')
        total_sessions = completed_sessions.count()
        total_duration = completed_sessions.aggregate(total=Sum('duration_seconds'))['total'] or 0

        # Category breakdown
        category_breakdown = []
        cat_stats = progress_records.values(
            'game__category__slug', 'game__category__title'
        ).annotate(
            games_played=Sum('completed_count'),
            stars=Sum('best_score')
        ).order_by('game__category__title')

        for stat in cat_stats:
            if stat['game__category__slug']:
                category_breakdown.append({
                    "category_slug": stat['game__category__slug'],
                    "category_title": stat['game__category__title'],
                    "games_played": stat['games_played'] or 0,
                    "stars": stat['stars'] or 0
                })

        # Recent activities (last 5)
        recent_records = progress_records.order_by('-last_played_at')[:5]
        recent_activity = [
            {
                "game_slug": rec.game.slug,
                "game_title": rec.game.title,
                "completed_count": rec.completed_count,
                "best_score": rec.best_score,
                "last_played_at": rec.last_played_at.isoformat() if rec.last_played_at else None
            }
            for rec in recent_records
        ]

        return Response({
            "child_id": str(child.id),
            "display_name": child.display_name,
            "age_band": child.age_band,
            "total_games_played": total_games_played,
            "total_stars": total_stars,
            "total_sessions_completed": total_sessions,
            "total_play_time_seconds": total_duration,
            "category_breakdown": category_breakdown,
            "recent_activity": recent_activity
        })
