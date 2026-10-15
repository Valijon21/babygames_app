from django.urls import path
from .views import GameContentView, UzbekAlphabetView, MathTasksView

urlpatterns = [
    path('games/<slug:slug>/content/', GameContentView.as_view(), name='game-content'),
    path('alphabet/', UzbekAlphabetView.as_view(), name='uzbek-alphabet'),
    path('math/tasks/', MathTasksView.as_view(), name='math-tasks'),
]
