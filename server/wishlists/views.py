from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Wishlist
from .serializers import WishlistsSerializers
from rest_framework.exceptions import ValidationError

# Create your views here.
class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistsSerializers
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        product = serializer.validated_data['product']

        if Wishlist.objects.filter(
            user=user,
            product=product
        ).exists():
            raise ValidationError(
                {
                    "detail": f"Rec with user {user.id} and {product.id} already exists"
                }
            )
        serializer.save(user=user)
