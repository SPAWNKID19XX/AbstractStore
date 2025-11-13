from rest_framework import routers
from .views import CustomProductViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r"", CustomProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),  # ViewSet
]
