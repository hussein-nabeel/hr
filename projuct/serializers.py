from rest_framework import serializers
from .models import Product,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields=['id','name','slug']

class ProductSerializer(serializers.ModelSerializer):
    image= serializers.ImageField(required=False)
    class Meta:
        model = Product
        fields=['id','category','name','slug','description','price','created_at','image'] 