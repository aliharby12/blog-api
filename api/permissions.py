from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    message = 'You Do not have permissions to do that'
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
