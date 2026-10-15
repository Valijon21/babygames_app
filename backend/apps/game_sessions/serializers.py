from rest_framework import serializers
from .models import GameSession
from apps.catalog.models import Game


class SessionStartSerializer(serializers.Serializer):
    game_slug = serializers.CharField(required=True)
    child_profile_id = serializers.UUIDField(required=False, allow_null=True)

    def validate_game_slug(self, value):
        try:
            game = Game.objects.get(slug=value, status='published')
        except Game.DoesNotExist:
            raise serializers.ValidationError("Belgilangan o‘yin mavjud emas yoki hali nashr etilmagan.")
        return game


class SessionCompleteSerializer(serializers.Serializer):
    completed = serializers.BooleanField(default=True)
    duration_seconds = serializers.IntegerField(min_value=0, max_value=86400, required=True)
    score = serializers.IntegerField(min_value=0, max_value=10000, required=False, allow_null=True)
    attempts = serializers.IntegerField(min_value=0, max_value=1000, required=False, default=1)
    content_version = serializers.IntegerField(min_value=1, default=1)
    result_summary = serializers.DictField(required=False, default=dict)


class GameSessionSerializer(serializers.ModelSerializer):
    game_title = serializers.CharField(source='game.title', read_only=True)
    game_slug = serializers.CharField(source='game.slug', read_only=True)

    class Meta:
        model = GameSession
        fields = [
            'id',
            'game_slug',
            'game_title',
            'child_profile',
            'started_at',
            'completed_at',
            'duration_seconds',
            'status',
            'score',
            'result_summary',
            'content_version'
        ]
        read_only_fields = ['id', 'started_at']
