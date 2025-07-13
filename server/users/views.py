from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .permitions import IsSuperuserOrCreate
from .serializers import UserSerializer
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyCustomTokenObtainPairSerializer

class UserViewSet(ModelViewSet):
    permission_classes = [IsSuperuserOrCreate]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class MyCustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyCustomTokenObtainPairSerializer