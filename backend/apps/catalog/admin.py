from django.contrib import admin
from .models import GameCategory, Game


@admin.register(GameCategory)
class GameCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'sort_order', 'is_active', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('sort_order', 'is_active')
    search_fields = ('title', 'slug')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'difficulty', 'min_age', 'max_age', 'status', 'content_version')
    list_filter = ('status', 'category', 'difficulty')
    search_fields = ('title', 'slug', 'description')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status', 'difficulty')
    readonly_fields = ('created_at', 'updated_at')
