from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from django.db.models import Q
from drf_spectacular.utils import extend_schema, OpenApiParameter
from .models import GameCategory, Game
from .serializers import GameCategorySerializer, GameListSerializer, GameDetailSerializer
from apps.common.cache import safe_cache_get, safe_cache_set, get_cache_version


class CategoryListView(generics.ListAPIView):
    """
    List all active game categories.
    Cached with versioned keys; automatically falls back if Redis is offline (BJ-128).
    """
    permission_classes = [AllowAny]
    serializer_class = GameCategorySerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        version = get_cache_version('catalog')
        cache_key = f"bolajon:v{version}:categories:active"
        cached_data = safe_cache_get(cache_key)

        if cached_data is not None:
            return Response(cached_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        safe_cache_set(cache_key, data, timeout=600)
        return Response(data)

    def get_queryset(self):
        return GameCategory.objects.filter(is_active=True).order_by('sort_order', 'title')


class GameListView(generics.ListAPIView):
    """
    Public catalog listing of published educational games.
    Supports filtering by category slug, target age, and difficulty.
    Uses select_related to guarantee 0 N+1 database queries.
    """
    permission_classes = [AllowAny]
    serializer_class = GameListSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter('category', str, description='Category slug to filter by'),
            OpenApiParameter('age', int, description='Child age to filter games within [min_age, max_age]'),
            OpenApiParameter('difficulty', str, description='Difficulty filter (easy, medium, hard)'),
            OpenApiParameter('search', str, description='Search by game title or description'),
        ]
    )
    def get_queryset(self):
        queryset = Game.objects.filter(status='published').select_related('category')

        # Filter by category slug
        category_slug = self.request.query_params.get('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        # Filter by age bracket
        age = self.request.query_params.get('age')
        if age:
            try:
                age_int = int(age)
                queryset = queryset.filter(min_age__lte=age_int, max_age__gte=age_int)
            except ValueError:
                pass

        # Filter by difficulty
        difficulty = self.request.query_params.get('difficulty')
        if difficulty in ['easy', 'medium', 'hard']:
            queryset = queryset.filter(difficulty=difficulty)

        # Search by title or description
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(description__icontains=search))

        return queryset.order_by('category__sort_order', 'title')


class GameDetailView(generics.RetrieveAPIView):
    """Retrieve full details of a specific published game by its unique slug."""
    permission_classes = [AllowAny]
    serializer_class = GameDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Game.objects.filter(status='published').select_related('category')


class GamePreviewView(generics.RetrieveAPIView):
    """
    BJ-103: Authoring preview endpoint for unpublished games (draft, review, archived).
    Restricted to staff content editors. Allows previewing content version prior to publication.
    """
    permission_classes = [IsAdminUser]
    serializer_class = GameDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        # Admins can preview any game regardless of publication status
        return Game.objects.all().select_related('category')
