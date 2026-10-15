from rest_framework import serializers
from .models import ChildProfile


class ChildProfileSerializer(serializers.ModelSerializer):
    age_band_display = serializers.CharField(source='get_age_band_display', read_only=True)

    class Meta:
        model = ChildProfile
        fields = [
            'id',
            'display_name',
            'age_band',
            'age_band_display',
            'avatar_key',
            'preferences',
            'is_active',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_preferences(self, value):
        """Enforce strict whitelist of allowed preference keys."""
        allowed_keys = {'sound_enabled', 'music_enabled', 'reduced_motion', 'theme'}
        if not isinstance(value, dict):
            raise serializers.ValidationError("Sozlamalar ob’ekt (JSON dictionary) bo‘lishi lozim.")
        for k in value.keys():
            if k not in allowed_keys:
                raise serializers.ValidationError(f"Ruxsat berilmagan sozlama kaliti: {k}")
        return value
