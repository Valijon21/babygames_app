from django.contrib import admin
from .models import GameAsset, ContentAuditEvent


@admin.register(GameAsset)
class GameAssetAdmin(admin.ModelAdmin):
    list_display = ('game', 'asset_type', 'storage_key', 'locale', 'created_at')
    list_filter = ('asset_type', 'locale')
    search_fields = ('game__title', 'storage_key', 'alt_text')


@admin.register(ContentAuditEvent)
class ContentAuditEventAdmin(admin.ModelAdmin):
    list_display = ('game', 'action', 'user', 'created_at')
    list_filter = ('action', 'created_at')
    search_fields = ('game__title', 'action', 'user__username')
    readonly_fields = ('game', 'user', 'action', 'details', 'created_at', 'updated_at')

    def has_add_permission(self, request):
        return False  # Immutable audit log cannot be manually added

    def has_delete_permission(self, request, obj=None):
        return False  # Immutable audit log cannot be manually deleted
