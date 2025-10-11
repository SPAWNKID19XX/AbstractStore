from rest_framework import routers
from .views import CustomUserViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r"", CustomUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls), name='user-list')
]
