from django.core.serializers import serialize
from django.template.defaulttags import comment
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .permissions import IsSuperuser
from rest_framework import viewsets
from .models import CustomProduct, ProductComments
from .serializers import ProductSerializer, ProductCommentSerializer

class CustomProductViewSet(viewsets.ModelViewSet):
    queryset = CustomProduct.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSuperuser]

    @action(
        detail=True,
        methods=["get", "post"],
        url_path="comments",
        permission_classes=[permissions.IsAuthenticatedOrReadOnly],
    )
    def comments(self, request, pk=None):
        product = self.get_object()

        if request.method.lower() == "get":
            comments = ProductComments.objects.filter(product=product)
            serializer = ProductCommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


        serializer = ProductCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        comment = serializer.save(
            product=product,
            user=request.user,
        )

        return Response(
            ProductCommentSerializer(comment).data,
            status=status.HTTP_201_CREATED,
        )

