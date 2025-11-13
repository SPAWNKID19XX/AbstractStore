from rest_framework import permissions

class IsSuperuser(permissions.BasePermission):
    '''
    permission for superusers
    '''
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    CRUD Products Comments
    """
    def has_permission(self, request, view):
        return