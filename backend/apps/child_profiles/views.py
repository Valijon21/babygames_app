from rest_framework import viewsets, permissions
from .models import ChildProfile
from .serializers import ChildProfileSerializer
from .permissions import IsGuardianOfChild


class ChildProfileViewSet(viewsets.ModelViewSet):
    """
    CRUD ViewSet for managing Child Profiles under the authenticated Guardian.
    """
    serializer_class = ChildProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsGuardianOfChild]

    def get_queryset(self):
        # Automatically scopes queries to the currently authenticated guardian
        return ChildProfile.objects.filter(guardian=self.request.user, is_active=True)

    def perform_create(self, serializer):
        serializer.save(guardian=self.request.user)

    def perform_destroy(self, instance):
        # Soft-delete by setting is_active=False or hard delete according to privacy policy
        instance.is_active = False
        instance.save()
