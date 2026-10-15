from django.urls import path
from .views import ChildProgressListView, ChildProgressSummaryView

urlpatterns = [
    path('children/<uuid:child_id>/', ChildProgressListView.as_view(), name='child-progress'),
    path('children/<uuid:child_id>/summary/', ChildProgressSummaryView.as_view(), name='child-progress-summary'),
]
