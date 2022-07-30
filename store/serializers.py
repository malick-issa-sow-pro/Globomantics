from rest_framework import serializers
from .models import Product, Category


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name_product', 'available', 'price', 'category')


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name_category')
