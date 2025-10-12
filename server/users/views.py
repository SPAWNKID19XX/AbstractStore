from django.http import HttpResponse

from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer



class CustomUserViewSet(viewsets.ModelViewSet):
    '''
    get=is_superuser
    post=anyone
    put, updatepartial = IsAuthenticated
    '''
    # todo login,signin permitions for is_superuser,
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]


    