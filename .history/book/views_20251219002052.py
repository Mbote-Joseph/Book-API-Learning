from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class BooksList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    