from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel


class GameAsset(TimeStampedModel):
    """Media and structured schema asset attached to an educational game."""
    ASSET_TYPE_CHOICES = [
        ('svg', 'SVG Vector Grafika'),
        ('png', 'PNG Rasm'),
        ('audio', 'Audio Ovoz'),
        ('json', 'JSON Sxema / Konfiguratsiya'),
    ]

    game = models.ForeignKey(
        'catalog.Game',
        on_delete=models.CASCADE,
        related_name='assets',
        verbose_name=_('O‘yin')
    )
    asset_type = models.CharField(max_length=16, choices=ASSET_TYPE_CHOICES)
    storage_key = models.CharField(max_length=255, help_text=_('Fayl yo‘li yoki CDN kaliti'))
    alt_text = models.CharField(max_length=255, blank=True)
    locale = models.CharField(max_length=8, default='uz')
    metadata = models.JSONField(default=dict, blank=True, help_text=_(
        'O‘yin asset metadata (region IDs, duration, viewBox)'))
    checksum = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name = _('O‘yin asseti')
        verbose_name_plural = _('O‘yin assetlari')

    def __str__(self):
        return f"{self.game.slug} — {self.asset_type} ({self.storage_key})"


class ContentAuditEvent(TimeStampedModel):
    """
    BJ-104: Immutable audit trail for all content status changes, publishing, and version bumps.
    Guarantees accountability and transparency in content moderation.
    """
    ACTION_CHOICES = [
        ('created', 'Yaratildi'),
        ('status_change', 'Status o‘zgartirildi'),
        ('updated', 'Tahrirlandi'),
        ('version_bump', 'Versiya oshirildi'),
    ]

    game = models.ForeignKey(
        'catalog.Game',
        on_delete=models.CASCADE,
        related_name='audit_events',
        verbose_name=_('O‘yin')
    )
    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='content_audits',
        verbose_name=_('Foydalanuvchi')
    )
    action = models.CharField(max_length=32, choices=ACTION_CHOICES)
    details = models.JSONField(default=dict, blank=True)

    class Meta:
        verbose_name = _('Kontent audit yozuvi')
        verbose_name_plural = _('Kontent audit yozuvlari')
        ordering = ['-created_at']

    def __str__(self):
        return f"Audit: {self.game.slug} [{self.action}] at {self.created_at}"
