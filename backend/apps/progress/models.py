from django.db import models
from django.utils.translation import gettext_lazy as _


class ProgressRecord(models.Model):
    """
    Cumulative progress and mastery metric for a child on a specific educational game.
    Strict unique constraint per (child_profile, game).
    """
    child_profile = models.ForeignKey(
        'child_profiles.ChildProfile',
        on_delete=models.CASCADE,
        related_name='progress_records',
        verbose_name=_('Bola profili')
    )
    game = models.ForeignKey(
        'catalog.Game',
        on_delete=models.CASCADE,
        related_name='progress_records',
        verbose_name=_('O‘yin')
    )
    completed_count = models.PositiveIntegerField(default=0, verbose_name=_('O‘ynalgan soni'))
    best_score = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Eng yuqori ball'))
    last_played_at = models.DateTimeField(auto_now=True, verbose_name=_('Oxirgi o‘ynalgan vaqt'))
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('O‘rganish natijasi')
        verbose_name_plural = _('O‘rganish natijalari')
        constraints = [
            models.UniqueConstraint(fields=['child_profile', 'game'], name='unique_child_game_progress')
        ]
        ordering = ['-last_played_at']

    def __str__(self):
        return f"{self.child_profile.display_name} — {self.game.title} ({self.completed_count} marta)"
