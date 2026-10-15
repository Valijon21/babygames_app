from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import UUIDModel, TimeStampedModel


class GameSession(UUIDModel, TimeStampedModel):
    """
    Lifecycle tracking for an active or completed gameplay session.
    Anonymous play is permitted for public demos; child_profile is linked when authenticated.
    """
    STATUS_CHOICES = [
        ('started', 'Boshlangan'),
        ('completed', 'Yakunlangan'),
        ('abandoned', 'Tugallanmagan'),
    ]

    child_profile = models.ForeignKey(
        'child_profiles.ChildProfile',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='game_sessions',
        verbose_name=_('Bola profili')
    )
    game = models.ForeignKey(
        'catalog.Game',
        on_delete=models.CASCADE,
        related_name='sessions',
        verbose_name=_('O‘yin')
    )
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    duration_seconds = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='started')
    score = models.PositiveIntegerField(null=True, blank=True)
    result_summary = models.JSONField(
        default=dict,
        blank=True,
        help_text=_('Schema-validated result payload (attempts, stars, completed items).')
    )
    content_version = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = _('O‘yin sessiyasi')
        verbose_name_plural = _('O‘yin sessiyalari')
        ordering = ['-started_at']
        indexes = [
            models.Index(fields=['child_profile', 'started_at'], name='session_child_date_idx'),
            models.Index(fields=['game', 'status'], name='session_game_status_idx'),
        ]

    def __str__(self):
        return f"Session {self.id} — {self.game.title} ({self.get_status_display()})"
