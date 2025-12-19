from django.contrib import admin
from .models import Book

# Register your models here.
class AdminBook(admin.ModelAdmin):
    model = Book
    fields = ['name','description', 'author', 'isbn', 'is_published', 'created_on']
    list_display = ('name','description', 'author', 'isbn', 'is_published', 'created_on')
    search_fields = ('name','description', 'author', 'isbn', 'is_published', 'created_on')

admin.site.register(Book, AdminBook)