from django.urls import path, include
from .views import UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import CurrentUserView
from .views import MyCustomTokenObtainPairView

app_name = 'users'

router = DefaultRouter()
router.register(r'', UserViewSet, basename='users')

urlpatterns = [
    path('token/', MyCustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('me/', CurrentUserView.as_view(), name='current_user'),
    path('', include(router.urls)),
]
