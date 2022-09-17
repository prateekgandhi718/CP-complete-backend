from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from base.models import Factory, Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'factory', 'title', 'quantity', 'description', 'image')

class FactorySerializer(ModelSerializer):
    productsInFactory=ProductSerializer(many=True)
    class Meta:
        model = Factory
        fields = ('id', 'factory_name', 'factory_location', 'productsInFactory')


