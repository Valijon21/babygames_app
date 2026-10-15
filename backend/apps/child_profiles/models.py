from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel, UUIDModel


class ChildProfile(UUIDModel, TimeStampedModel):
    """
    Child Profile entity managed exclusively by a verified Guardian.
    Minimal PII: No real names required, no birth dates, only age bands.
    """
    AGE_BAND_CHOICES = [
        ('2-4', '2–4 yosh (Kichkintoylar)'),
        ('5-7', '5–7 yosh (Maktabgacha)'),
        ('8-10', '8–10 yosh (Boshlang‘ich)'),
        ('11-14', '11–14 yosh (O‘smirlar)'),
    ]

    guardian = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name=_('Vasiy / Ota-ona'),
        db_index=True
    )
    display_name = models.CharField(
        max_length=64,
        verbose_name=_('Taxallus / Ism'),
        help_text=_('Bolaning ismi yoki yoqimli taxallusi.')
    )
    age_band = models.CharField(
        max_length=16,
        choices=AGE_BAND_CHOICES,
        default='5-7',
        verbose_name=_('Yosh toifasi')
    )
    avatar_key = models.CharField(
        max_length=64,
        default='avatar_bear',
        verbose_name=_('Avatar kaliti')
    )
    preferences = models.JSONField(
        default=dict,
        blank=True,
        verbose_name=_('Sozlamalar (Ovoz, rang va h.k.)')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Faol')
    )

    class Meta:
        verbose_name = _('Bola profili')
        verbose_name_plural = _('Bolalar profillari')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.display_name} ({self.get_age_band_display()})"
