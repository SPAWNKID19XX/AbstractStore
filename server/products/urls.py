from rest_framework import routers
from .views import CustomProductViewSet
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = routers.DefaultRouter()

router.register(r"", CustomProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),  # ViewSet
]
