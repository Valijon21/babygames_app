from django.urls import path
from .views import ChildProgressListView

urlpatterns = [
    path('children/<uuid:child_id>/', ChildProgressListView.as_view(), name='child-progress'),
]
