from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.user and request.user == obj.user or request.method in permissions.SAFE_METHODS:
            return True

        return False
