from rest_framework import serializers
from .models import GameCategory, Game


class GameCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameCategory
        fields = ['id', 'slug', 'title', 'description', 'icon_key', 'sort_order']


class GameListSerializer(serializers.ModelSerializer):
    category_slug = serializers.CharField(source='category.slug', read_only=True)
    category_title = serializers.CharField(source='category.title', read_only=True)
    difficulty_display = serializers.CharField(source='get_difficulty_display', read_only=True)

    class Meta:
        model = Game
        fields = [
            'id',
            'slug',
            'title',
            'category_slug',
            'category_title',
            'min_age',
            'max_age',
            'difficulty',
            'difficulty_display',
            'thumbnail',
            'estimated_minutes',
            'content_version',
        ]


class GameDetailSerializer(serializers.ModelSerializer):
    category = GameCategorySerializer(read_only=True)
    difficulty_display = serializers.CharField(source='get_difficulty_display', read_only=True)

    class Meta:
        model = Game
        fields = [
            'id',
            'slug',
            'title',
            'description',
            'category',
            'min_age',
            'max_age',
            'difficulty',
            'difficulty_display',
            'thumbnail',
            'estimated_minutes',
            'content_version',
            'published_at',
        ]
