from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    
    name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User     #User model to serialize
        fields = ['id','_id', 'username', 'email', 'name']      #will return everything/every info
        isAdmin = serializers.SerializerMethodField(read_only=True)
    
    def get__id(self, obj):
        return obj.id
    
    def get_isAdmin(self, obj):
        return obj.is_staff
    

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        
        return name

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product     #Product model to serialize
        fields = '__all__'      #will return everything/every products

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
