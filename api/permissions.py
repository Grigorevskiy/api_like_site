
from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.user and request.user == obj.user or request.method in permissions.SAFE_METHODS:
            return True
        return False


class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or request.user and request.user.is_staff
        )
