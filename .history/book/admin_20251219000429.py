from django.contrib import admin
from .models import Book

# Register your models here.
class AdminBook(admin.ModelAdmin):
    model = Book
    fields = ['name','description', 'author', 'isbn', 'is_published', 'created_on',]

admin.site.register(Book, AdminBook)