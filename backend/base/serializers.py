from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product


class UserSerializer(serializers.ModelSerializer):
    
    name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User     #User model to serialize
        fields = ['id', 'username', 'email', 'name']      #will return everything/every info
    
    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        
        return name

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product     #Product model to serialize
        fields = '__all__'      #will return everything/every products
