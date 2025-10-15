from rest_framework import permissions

class IsOwnerOrSuperuser(permissions.BasePermission):
    '''
    Custom permitions for Owners or Superusers
    '''

    def has_object_permission(self, request, view, obj):
        return request.user and (obj == request.user or request.user.is_superuser)