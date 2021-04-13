from django.contrib.auth.models import User, update_last_login
from django.db.models import manager
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
# from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer, UserSerializer, UserSerializerWithToken

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        # data['username'] = self.user.username
        # data['email'] = self.user.email 
        
        serializer = UserSerializerWithToken(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data

    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['message'] = 'hello world'
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/products/',
        'api/products/create'
    ]
    # return JsonResponse(routes, safe=False)
    return Response(routes)

@api_view(['GET'])
def getUserProfile(request):
    user = request.user
    # return JsonResponse(products, safe=False)
    # products = Product.objects.all()
    
    serializer = UserSerializer(user, many = False)   #many=true means multiple objects
    
    return Response(serializer.data)

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
