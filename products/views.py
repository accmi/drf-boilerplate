from rest_framework import generics, permissions

from .models import Maker, Product, ProductCategory
from .serializers import (
    MakerSerializer,
    ProductCategorySerializer,
    ProductSerializer,
)


class ProductCategoryListCreateView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductCategoryRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class MakerListCreateView(generics.ListCreateAPIView):
    queryset = Maker.objects.all()
    serializer_class = MakerSerializer
    permission_classes = [permissions.IsAuthenticated]


class MakerRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = Maker.objects.all()
    serializer_class = MakerSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
