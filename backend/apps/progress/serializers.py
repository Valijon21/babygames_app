from rest_framework import serializers
from .models import ProgressRecord


class ProgressRecordSerializer(serializers.ModelSerializer):
    game_title = serializers.CharField(source='game.title', read_only=True)
    game_slug = serializers.CharField(source='game.slug', read_only=True)
    category_title = serializers.CharField(source='game.category.title', read_only=True)

    class Meta:
        model = ProgressRecord
        fields = [
            'id',
            'game_slug',
            'game_title',
            'category_title',
            'completed_count',
            'best_score',
            'last_played_at',
            'updated_at'
        ]
