from rest_framework import serializers
from .models import CustomProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomProduct
        fields = [
            "id",
            "title",
            "description"
        ]
