from rest_framework import routers
from django.urls import path, include
from .views import WishlistViewSet


router = routers.DefaultRouter()

router.register(r"", WishlistViewSet, basename='wishlist')

urlpatterns = [
    path('', include(router.urls)),
]
