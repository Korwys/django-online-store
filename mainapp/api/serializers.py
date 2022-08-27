from rest_framework import serializers

from cartapp.models import Cart
from orderapp.models import Order
from productapp.models import Product, Brand, ProductCategory, Genders
from wishapp.models import WishList


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'description')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'brand', 'price', 'gender')


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genders
        fields = ('name',)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'created_at', 'updated_at', 'status')


class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = WishList
        fields = ('product',)


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = ('product', 'quantity')
