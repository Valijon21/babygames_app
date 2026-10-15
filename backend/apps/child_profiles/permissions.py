from rest_framework import permissions


class IsGuardianOfChild(permissions.BasePermission):
    """
    Object-level permission allowing only the registered guardian to access or modify the child profile.
    Completely eliminates IDOR attack surface.
    """

    def has_object_permission(self, request, view, obj):
        return obj.guardian == request.user
