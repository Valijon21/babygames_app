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

    def submit_for_review(self, user=None):
        """BJ-101: Transition from draft to review."""
        if self.status != 'draft':
            raise ValueError(f"Faqat 'draft' holatidagi o‘yin tekshiruvga yuborilishi mumkin. Hozirgi: {self.status}")
        self.status = 'review'
        self.save()
        self._record_audit(user, 'status_change', {"from": "draft", "to": "review"})

    def publish(self, user=None):
        """BJ-101: Transition from review (or draft) to published with cache invalidation."""
        from django.utils import timezone
        from apps.common.cache import invalidate_catalog_cache

        prev_status = self.status
        self.status = 'published'
        self.published_at = timezone.now()
        self.content_version += 1
        self.save()

        # Invalidate catalog cache so clients see fresh content immediately
        invalidate_catalog_cache()
        self._record_audit(user, 'status_change', {
            "from": prev_status,
            "to": "published",
            "version": self.content_version
        })

    def archive(self, user=None):
        """BJ-101: Transition to archived."""
        from apps.common.cache import invalidate_catalog_cache

        prev_status = self.status
        self.status = 'archived'
        self.save()
        invalidate_catalog_cache()
        self._record_audit(user, 'status_change', {"from": prev_status, "to": "archived"})

    def bump_version(self, user=None, reason=""):
        """BJ-103: Increment content version and invalidate cache."""
        from apps.common.cache import invalidate_catalog_cache

        self.content_version += 1
        self.save()
        invalidate_catalog_cache()
        self._record_audit(user, 'version_bump', {"new_version": self.content_version, "reason": reason})

    def _record_audit(self, user, action, details):
        """Internal helper to log ContentAuditEvent without circular import."""
        try:
            from apps.game_content.models import ContentAuditEvent
            ContentAuditEvent.objects.create(
                game=self,
                user=user if user and user.is_authenticated else None,
                action=action,
                details=details
            )
        except Exception:
            pass
