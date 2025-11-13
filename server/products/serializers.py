from rest_framework import serializers
from .models import CustomProduct, ProductComments


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomProduct
        fields = [
            "id",
            "title",
            "description"
        ]


class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComments
        fields = [
            "id",
            "user",
            "product",
            "comment",
            "rating",
            "published_at",
            "updated_at"
        ]
        read_only_fields = [
            "id",
            "user",
            "product",
            "published_at",
            "updated_at"
        ]

