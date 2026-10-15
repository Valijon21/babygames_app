from django.contrib import admin
from .models import ProgressRecord


@admin.register(ProgressRecord)
class ProgressRecordAdmin(admin.ModelAdmin):
    list_display = ('child_profile', 'game', 'completed_count', 'best_score', 'last_played_at')
    list_filter = ('game', 'last_played_at')
    search_fields = ('child_profile__display_name', 'game__title')
    readonly_fields = ('last_played_at', 'updated_at')
