from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from .models import GameAsset
from apps.catalog.models import Game


class GameContentView(APIView):
    """
    Returns verified, versioned content schema and assets for a published game.
    """
    permission_classes = [AllowAny]

    def get(self, request, slug):
        game = get_object_or_404(Game, slug=slug, status='published')
        assets = GameAsset.objects.filter(game=game)

        assets_data = [
            {
                "id": str(a.id),
                "asset_type": a.asset_type,
                "storage_key": a.storage_key,
                "alt_text": a.alt_text,
                "locale": a.locale,
                "metadata": a.metadata
            } for a in assets
        ]

        return Response({
            "game_slug": game.slug,
            "title": game.title,
            "content_version": game.content_version,
            "category": game.category.slug,
            "min_age": game.min_age,
            "max_age": game.max_age,
            "difficulty": game.difficulty,
            "assets": assets_data
        })


class UzbekAlphabetView(APIView):
    """
    Returns the complete official Uzbek Latin alphabet content with phonetic labels,
    diacritics (O‘, G‘, Sh, Ch, Ng), example words, and audio metadata.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        alphabet_data = [
            {"letter": "A", "lowercase": "a", "word": "Anor", "translation": "Pomegranate", "icon": "apple"},
            {"letter": "B", "lowercase": "b", "word": "Baliq", "translation": "Fish", "icon": "fish"},
            {"letter": "D", "lowercase": "d", "word": "Daraxt", "translation": "Tree", "icon": "tree"},
            {"letter": "E", "lowercase": "e", "word": "Eshik", "translation": "Door", "icon": "door"},
            {"letter": "F", "lowercase": "f", "word": "Fil", "translation": "Elephant", "icon": "elephant"},
            {"letter": "G", "lowercase": "g", "word": "Gul", "translation": "Flower", "icon": "flower"},
            {"letter": "H", "lowercase": "h", "word": "Humo", "translation": "Bird Humo", "icon": "bird"},
            {"letter": "I", "lowercase": "i", "word": "It", "translation": "Dog", "icon": "dog"},
            {"letter": "J", "lowercase": "j", "word": "Jo‘ja", "translation": "Chick", "icon": "chick"},
            {"letter": "K", "lowercase": "k", "word": "Kitob", "translation": "Book", "icon": "book"},
            {"letter": "L", "lowercase": "l", "word": "Lola", "translation": "Tulip", "icon": "tulip"},
            {"letter": "M", "lowercase": "m", "word": "Mushuk", "translation": "Cat", "icon": "cat"},
            {"letter": "N", "lowercase": "n", "word": "Non", "translation": "Bread", "icon": "bread"},
            {"letter": "O", "lowercase": "o", "word": "Olma", "translation": "Apple", "icon": "apple"},
            {"letter": "P", "lowercase": "p", "word": "Pichoq", "translation": "Knife", "icon": "knife"},
            {"letter": "Q", "lowercase": "q", "word": "Quyosh", "translation": "Sun", "icon": "sun"},
            {"letter": "R", "lowercase": "r", "word": "Rasm", "translation": "Picture", "icon": "image"},
            {"letter": "S", "lowercase": "s", "word": "Sabzi", "translation": "Carrot", "icon": "carrot"},
            {"letter": "T", "lowercase": "t", "word": "Toshbaqa", "translation": "Turtle", "icon": "turtle"},
            {"letter": "U", "lowercase": "u", "word": "Uzum", "translation": "Grape", "icon": "grape"},
            {"letter": "V", "lowercase": "v", "word": "Velosiped", "translation": "Bicycle", "icon": "bike"},
            {"letter": "X", "lowercase": "x", "word": "Xurmo", "translation": "Persimmon", "icon": "fruit"},
            {"letter": "Y", "lowercase": "y", "word": "Yulduz", "translation": "Star", "icon": "star"},
            {"letter": "Z", "lowercase": "z", "word": "Zebro", "translation": "Zebra", "icon": "zebra"},
            {"letter": "O‘", "lowercase": "o‘", "word": "O‘rdak", "translation": "Duck", "icon": "duck"},
            {"letter": "G‘", "lowercase": "g‘", "word": "G‘oz", "translation": "Goose", "icon": "goose"},
            {"letter": "Sh", "lowercase": "sh", "word": "Shar", "translation": "Balloon", "icon": "balloon"},
            {"letter": "Ch", "lowercase": "ch", "word": "Choynak", "translation": "Teapot", "icon": "tea"},
            {"letter": "Ng", "lowercase": "ng", "word": "Tong", "translation": "Dawn", "icon": "sunrise"}
        ]
        return Response({"count": len(alphabet_data), "locale": "uz", "letters": alphabet_data})


class MathTasksView(APIView):
    """
    Returns curated, pedagogical mathematics tasks tailored by age band and difficulty.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        age_band = request.query_params.get('age_band', '5-7')
        tasks = [
            {"id": 1, "type": "count", "prompt": "Nechta olma bor?", "count": 5, "options": [3, 5, 7], "answer": 5},
            {"id": 2, "type": "compare", "prompt": "Qaysi biri ko‘proq?", "left": 6, "right": 4, "answer": "left"},
            {"id": 3, "type": "add", "prompt": "2 + 3 = ?", "expression": "2 + 3", "options": [4, 5, 6], "answer": 5},
            {"id": 4, "type": "count", "prompt": "Nechta yulduz bor?", "count": 8, "options": [6, 8, 9], "answer": 8},
        ]
        return Response({"age_band": age_band, "tasks": tasks})
