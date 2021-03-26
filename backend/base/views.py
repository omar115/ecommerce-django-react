from django.db.models import manager
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/products/',
        'api/products/create'
    ]
    # return JsonResponse(routes, safe=False)
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    # return JsonResponse(products, safe=False)
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True)   #many=true means multiple objects
    
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    # return JsonResponse(products, safe=False)
    # product = None
    # for i in products:
    #     if i['_id'] == pk:
    #         product = i
    #         break
    product = Product.objects.get(_id = pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
