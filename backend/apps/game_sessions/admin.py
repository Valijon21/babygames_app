from django.contrib import admin
from .models import GameSession


@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'child_profile', 'status', 'score', 'duration_seconds', 'started_at')
    list_filter = ('status', 'game')
    search_fields = ('id', 'game__title', 'child_profile__display_name')
    readonly_fields = ('id', 'started_at', 'completed_at')
