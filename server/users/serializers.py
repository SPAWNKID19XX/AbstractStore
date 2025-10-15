from .models import CustomUser
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "full_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "password"
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
