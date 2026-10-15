from django.urls import path
from .views import SessionStartView, SessionCompleteView

urlpatterns = [
    path('', SessionStartView.as_view(), name='session-start'),
    path('<uuid:pk>/complete/', SessionCompleteView.as_view(), name='session-complete'),
]
