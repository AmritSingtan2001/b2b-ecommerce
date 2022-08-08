from unicodedata import category
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAdminOrReadOnly
from .serializers import (CategorySerializer,
                        SubCategorySerializer, 
                        SubSubCategorySerializer, 
                        ProductSerializer,
                        BrandSerializer)
from .models import Category, SubCategory, SubSubCategory, Product, Brand

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class SubCategoryViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class SubSubCategoryViewSet(ModelViewSet):
    queryset = SubSubCategory.objects.all()
    serializer_class = SubSubCategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminOrReadOnly]