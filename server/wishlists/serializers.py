from rest_framework import serializers
from .models import Wishlist

class WishlistsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = [
            "id",
            "user",
            "product"
        ]