from rest_framework import permissions

class IsOwnerOrSuperuser(permissions.BasePermission):
    '''
    Custom permitions for Owners or Superusers
    '''

    def has_object_permission(self, request, view, obj):

        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        return obj == request.user