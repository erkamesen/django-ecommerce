from rest_framework.response import Response
from product.rest.serializers import (
    ProductSerializer,
    CategorySerializer,
    BrandSerializer,
)
from product.models import (
    Product,
    Category,
    Brand
)
from rest_framework import viewsets
from rest_framework import status
from drf_spectacular.utils import extend_schema
# Create your views here.


class CategoryListCreateView(viewsets.ViewSet):
    """
    Viewset for viewing all categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer,
                   request=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(responses=CategorySerializer,
                   request=CategorySerializer)
    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
