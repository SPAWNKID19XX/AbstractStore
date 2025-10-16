from .permissions import IsSuperuser
from rest_framework import viewsets

from .models import CustomProduct
from .serializers import ProductSerializer

class CustomProductViewSet(viewsets.ModelViewSet):
    queryset = CustomProduct.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSuperuser]