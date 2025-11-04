from rest_framework import routers
from .views import CustomUserViewSet
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = routers.DefaultRouter()

router.register(r"", CustomUserViewSet, basename='users')

urlpatterns = [

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('API/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),  # ViewSet
]
