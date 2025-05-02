from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, user_data):
        return (
            request.method in SAFE_METHODS
            or user_data.author == request.user)
