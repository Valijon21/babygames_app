from django.contrib import admin
from .models import ChildProfile


@admin.register(ChildProfile)
class ChildProfileAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'guardian', 'age_band', 'avatar_key', 'is_active', 'created_at')
    list_filter = ('age_band', 'is_active')
    search_fields = ('display_name', 'guardian__email')
    readonly_fields = ('id', 'created_at', 'updated_at')
