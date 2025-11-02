from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Wishlist
from .serializers import WishlistsSerializers

# Create your views here.
class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistsSerializers
    permission_classes = [permissions.IsAuthenticated]

