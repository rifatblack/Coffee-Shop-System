from rest_framework import permissions

class IsBaristaOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        """
        Custom permission to only allow the users with food.can_serve permission
        """
        
        return request.user.has_perm('food.can_serve')
