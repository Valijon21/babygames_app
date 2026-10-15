from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from apps.catalog.models import GameCategory, Game


class CatalogAPITests(TestCase):
    def setUp(self):
        self.category = GameCategory.objects.create(
            slug='coloring',
            title='Rasm bo‘yash',
            sort_order=1
        )
        self.game = Game.objects.create(
            category=self.category,
            slug='test-coloring',
            title='Test Bo‘yash',
            min_age=3,
            max_age=6,
            difficulty='easy',
            status='published'
        )
        self.draft_game = Game.objects.create(
            category=self.category,
            slug='draft-game',
            title='Qoralama O‘yin',
            status='draft'
        )

    def test_list_categories(self):
        url = reverse('category-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['slug'], 'coloring')

    def test_list_published_games_excludes_draft(self):
        url = reverse('game-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json()['results']
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['slug'], 'test-coloring')

    def test_game_detail(self):
        url = reverse('game-detail', kwargs={'slug': 'test-coloring'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], 'Test Bo‘yash')
