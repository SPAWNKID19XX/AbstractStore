from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)