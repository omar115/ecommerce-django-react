from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User     #User model to serialize
        fields = ['id', 'username', 'email']      #will return everything/every info

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product     #Product model to serialize
        fields = '__all__'      #will return everything/every products
