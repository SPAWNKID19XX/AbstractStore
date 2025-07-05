from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'password',
            'email',
            'full_name',
            "phone",
            "address",
            "gender",
            "date_of_birth",
            "is_active",
            "is_staff",
            "is_superuser",
            "tax_id"
        )

    def get_full_name(self, obj):
        return obj.get_full_name()

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        if password is None:
            raise serializers.ValidationError('Password is required')
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.tax_id = validated_data.get('tax_id', instance.tax_id)

        password = validated_data.get('password',None)

        if password:
            instance.set_password(password)

        instance.save()
        return instance

