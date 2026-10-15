from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.catalog.models import GameCategory, Game


class Command(BaseCommand):
    help = 'Seeds initial educational game categories and MVP games idempotently.'

    def handle(self, *args, **options):
        self.stdout.write('Seeding Bolajon educational game catalog...')

        # 1. Categories
        categories_data = [
            {
                'slug': 'coloring',
                'title': 'Rasm bo‘yash',
                'description': 'Hayvonlar, tabiat va qahramonlarni rang-barang bo‘yash.',
                'icon_key': 'icon_palette',
                'sort_order': 1,
            },
            {
                'slug': 'alphabet',
                'title': 'O‘zbek alifbosi',
                'description': 'Harflarni tanish, to‘g‘ri talaffuz va izidan yozish.',
                'icon_key': 'icon_abc',
                'sort_order': 2,
            },
            {
                'slug': 'numbers',
                'title': 'Raqamlar va hisob',
                'description': 'Sanash, taqqoslash va boshlang‘ich matematik qiziqarli o‘yinlar.',
                'icon_key': 'icon_123',
                'sort_order': 3,
            },
            {
                'slug': 'memory',
                'title': 'Xotira va diqqat',
                'description': 'Juft kartalarni topish, ketma-ketlikni eslab qolish.',
                'icon_key': 'icon_brain',
                'sort_order': 4,
            },
        ]

        category_map = {}
        for cat in categories_data:
            obj, created = GameCategory.objects.update_or_create(
                slug=cat['slug'],
                defaults={
                    'title': cat['title'],
                    'description': cat['description'],
                    'icon_key': cat['icon_key'],
                    'sort_order': cat['sort_order'],
                    'is_active': True,
                }
            )
            category_map[cat['slug']] = obj
            status_text = 'Created' if created else 'Updated'
            self.stdout.write(f"  [{status_text}] Category: {obj.title}")

        # 2. Games
        games_data = [
            {
                'category': category_map['coloring'],
                'slug': 'coloring-animals',
                'title': 'Hayvonlar olami',
                'description': 'Mushukcha, quyoncha, qushcha va boshqa do‘stlarimizni bo‘yang.',
                'min_age': 2,
                'max_age': 7,
                'difficulty': 'easy',
                'thumbnail': '/assets/thumbnails/coloring-animals.svg',
                'estimated_minutes': 5,
                'status': 'published',
                'content_version': 1,
            },
            {
                'category': category_map['alphabet'],
                'slug': 'alphabet-trace',
                'title': 'Sehrli harflar',
                'description': 'Harflarni eshitamiz, taniymiz va chiroyli yozishni o‘rganamiz.',
                'min_age': 4,
                'max_age': 8,
                'difficulty': 'easy',
                'thumbnail': '/assets/thumbnails/alphabet-trace.svg',
                'estimated_minutes': 7,
                'status': 'published',
                'content_version': 1,
            },
            {
                'category': category_map['numbers'],
                'slug': 'numbers-count-10',
                'title': '1 dan 10 gacha sanash',
                'description': 'Mevalar va quvnoq buyumlarni sanab to‘g‘ri raqamni toping.',
                'min_age': 3,
                'max_age': 6,
                'difficulty': 'easy',
                'thumbnail': '/assets/thumbnails/numbers-count.svg',
                'estimated_minutes': 5,
                'status': 'published',
                'content_version': 1,
            },
            {
                'category': category_map['memory'],
                'slug': 'memory-animals',
                'title': 'Hayvonlar juftligi',
                'description': 'Bir xil hayvonlar tasvirlangan kartalarni toping va xotirani mustahkamlang.',
                'min_age': 3,
                'max_age': 8,
                'difficulty': 'easy',
                'thumbnail': '/assets/thumbnails/memory-animals.svg',
                'estimated_minutes': 6,
                'status': 'published',
                'content_version': 1,
            },
        ]

        now = timezone.now()
        for g in games_data:
            obj, created = Game.objects.update_or_create(
                slug=g['slug'],
                defaults={
                    'category': g['category'],
                    'title': g['title'],
                    'description': g['description'],
                    'min_age': g['min_age'],
                    'max_age': g['max_age'],
                    'difficulty': g['difficulty'],
                    'thumbnail': g['thumbnail'],
                    'estimated_minutes': g['estimated_minutes'],
                    'status': g['status'],
                    'content_version': g['content_version'],
                    'published_at': now,
                }
            )
            status_text = 'Created' if created else 'Updated'
            self.stdout.write(f"  [{status_text}] Game: {obj.title}")

        self.stdout.write(self.style.SUCCESS('Catalog seeded successfully!'))
