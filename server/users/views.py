from django.http import HttpResponse
from .permissions import IsOwnerOrSuperuser
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from .models import CustomUser
from .serializers import CustomUserSerializer



class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrSuperuser]

        return [permissions() for permissions in permission_classes]