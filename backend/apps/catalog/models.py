from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel


class GameCategory(TimeStampedModel):
    """Category grouping for educational games (e.g. Coloring, Alphabet, Numbers, Memory)."""
    slug = models.SlugField(max_length=64, unique=True, db_index=True)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    icon_key = models.CharField(max_length=64, default='category_default')
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('O‘yin kategoriyasi')
        verbose_name_plural = _('O‘yin kategoriyalari')
        ordering = ['sort_order', 'title']

    def __str__(self):
        return self.title


class Game(TimeStampedModel):
    """Educational game entity with age bounds, difficulty, and publication lifecycle."""
    DIFFICULTY_CHOICES = [
        ('easy', 'Oson'),
        ('medium', 'O‘rtacha'),
        ('hard', 'Qiyin'),
    ]

    STATUS_CHOICES = [
        ('draft', 'Qoralama'),
        ('review', 'Tekshiruvda'),
        ('published', 'Nashr etilgan'),
        ('archived', 'Arxivlangan'),
    ]

    category = models.ForeignKey(
        GameCategory,
        on_delete=models.PROTECT,
        related_name='games',
        verbose_name=_('Kategoriya')
    )
    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    min_age = models.PositiveSmallIntegerField(default=3)
    max_age = models.PositiveSmallIntegerField(default=7)
    difficulty = models.CharField(max_length=16, choices=DIFFICULTY_CHOICES, default='easy')
    thumbnail = models.CharField(max_length=255, blank=True, default='')
    estimated_minutes = models.PositiveSmallIntegerField(default=5)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='draft', db_index=True)
    content_version = models.PositiveIntegerField(default=1)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _('O‘yin')
        verbose_name_plural = _('O‘yinlar')
        ordering = ['title']
        indexes = [
            models.Index(fields=['status', 'category', 'min_age', 'max_age'], name='game_catalog_idx'),
        ]

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
