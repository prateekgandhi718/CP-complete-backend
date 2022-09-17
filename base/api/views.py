from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pathlib import Path
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser

# import the factory model now.
from base.models import Factory
#importing the serializer as well
from .serializers import FactorySerializer, ProductSerializer

#importing the product model.
from base.models import Product

from base.azure_file_controller import ALLOWED_EXTENTIONS, download_blob, upload_file_to_blob, delete_blob_client

@api_view(['GET'])
def getRoutes(request):
    routes = ['GET endpoint at /api that is home!',
              'GET endpoint at /api/factories to get the factories',
              'GET endpoint at /api/factories/:id to get details of a particular factory']
    return Response(routes)

@api_view(['GET', 'POST'])
def getFactories(request):
    if request.method == 'GET':
        factories = Factory.objects.all()
        serializer = FactorySerializer(factories, many = True) #this will be query set, therefore to display as JSON, use serializer. many=True just serializes all the objects
        return Response(serializer.data) 
    elif request.method == 'POST':
        serializer = FactorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def getAFactory(request, factoryId, format = None):
    if request.method == 'GET':
        try:
            products = Product.objects.filter(factory = factoryId)
        except Product.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        file = request.data['image']
        print(file.name)
        
        

        serializer = ProductSerializer(data = request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            new_file = upload_file_to_blob(file)
            print(new_file)
        
            request.data['image'].name = new_file
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes([MultiPartParser, FormParser])
def getAProduct(request, factoryId, productId, format = None):
    try:
        product = Product.objects.filter(factory = factoryId).get(id = productId)
    except Product.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product, many = False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            file = request.FILES['image']
                # print(type(file))
            #       ext = Path(file.name).suffix
            #       #     print(data['id'])
            #       #     print()

            new_file = upload_file_to_blob(file)
                # print(new_file)
            product.image.name = new_file
            request.data['image'].name = new_file
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = ProductSerializer(product, many=False)
        delete_blob_client(str(product.image.name))
        product.delete()
        return Response(serializer.data, status = status.HTTP_204_NO_CONTENT)
        


