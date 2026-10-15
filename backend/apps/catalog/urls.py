from django.urls import path
from .views import CategoryListView, GameListView, GameDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('games/', GameListView.as_view(), name='game-list'),
    path('games/<slug:slug>/', GameDetailView.as_view(), name='game-detail'),
]
