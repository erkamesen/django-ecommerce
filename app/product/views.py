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


class CategoryView(viewsets.ViewSet):
    """
    Viewset for viewing all categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer,
                   request=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BrandView(viewsets.ViewSet):
    """
    Viewset for viewing all brands
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer,
                   request=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductView(viewsets.ViewSet):
    """
    Viewset for viewing all products
    """

    queryset = Product.objects.all()
    lookup_field = "product_id"

    @extend_schema(responses=ProductSerializer,
                   request=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(responses=ProductSerializer,
                   request=ProductSerializer)
    def retrieve(self, request, product_id):
        product = self.queryset.get(id=product_id)
        serializer = ProductSerializer(instance=product)
        return Response(serializer.data, status=status.HTTP_200_OK)
