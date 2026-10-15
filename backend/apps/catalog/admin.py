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
    readonly_fields = ('created_at', 'updated_at', 'published_at', 'content_version')
    actions = ['publish_selected', 'submit_for_review_selected', 'archive_selected']

    @admin.action(description="Tanlangan o‘yinlarni nashr etish (Publish)")
    def publish_selected(self, request, queryset):
        for game in queryset:
            game.publish(user=request.user)
        self.message_user(request, f"{queryset.count()} ta o‘yin muvaffaqiyatli nashr etildi.")

    @admin.action(description="Tanlangan o‘yinlarni tekshiruvga yuborish (Review)")
    def submit_for_review_selected(self, request, queryset):
        for game in queryset:
            if game.status == 'draft':
                game.submit_for_review(user=request.user)
        self.message_user(request, "Tanlangan o‘yinlar tekshiruvga yuborildi.")

    @admin.action(description="Tanlangan o‘yinlarni arxivlash (Archive)")
    def archive_selected(self, request, queryset):
        for game in queryset:
            game.archive(user=request.user)
        self.message_user(request, "Tanlangan o‘yinlar arxivlandi.")

    def save_model(self, request, obj, form, change):
        if change and 'status' in form.changed_data:
            prev_status = form.initial.get('status')
            obj._record_audit(request.user, 'status_change', {
                "from": prev_status,
                "to": obj.status,
                "via": "django_admin"
            })
        super().save_model(request, obj, form, change)
