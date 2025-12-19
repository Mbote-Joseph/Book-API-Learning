from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    description = serializers.CharField(min_length=2, max_length=200)
    class Meta:
        model = Book
        fields = ('id', 'name', 'description', 'author', 'isbn','is_published', 'created_on')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"