from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer, UserSerializer

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from book.serializers import BookSerializer, UserSerializer
from django.contrib.auth.models import User

# Create your views here.
class BooksList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('id','name', 'description')
    search_fields = ['name','description',]
    
    
class BookCreate(CreateAPIView):
    serializer_class = BookSerializer
    
    
class BookRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"
    
    
class UsersList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter,]
    filterset_fields = ["username", "first_name", "last_name", "email"]
    search_fields = ["username", "first_name", "last_name", "email"]
    
    
    
    
    
class UserCreate(CreateAPIView):
    serializer_class = UserSerializer