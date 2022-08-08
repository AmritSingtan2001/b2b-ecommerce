from rest_framework import serializers

from .models import (Category, SubCategory, SubSubCategory, Product, Brand)

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products = ProductSerializer(many = True, read_only = True)
    class Meta:
        model = Category
        fields = ['id','name', 'products']

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SubCategory
        fields = '__all__'

class SubSubCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SubSubCategory
        fields = '__all__'

class BrandSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'