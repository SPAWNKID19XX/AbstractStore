from rest_framework import routers
from django.urls import path, include
from .views import WishlistViewSet


router = routers.DefaultRouter()

router.register(r"", WishlistViewSet, basename='wishlists')

urlpatterns = [
    path('', include(router.urls)),
]
