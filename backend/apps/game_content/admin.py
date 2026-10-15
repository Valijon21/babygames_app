from django.contrib import admin
from .models import GameAsset


@admin.register(GameAsset)
class GameAssetAdmin(admin.ModelAdmin):
    list_display = ('game', 'asset_type', 'storage_key', 'locale', 'created_at')
    list_filter = ('asset_type', 'locale')
    search_fields = ('game__title', 'storage_key', 'alt_text')
