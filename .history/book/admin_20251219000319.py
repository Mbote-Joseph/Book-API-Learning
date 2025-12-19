from django.contrib import admin
from .models import Book

# Register your models here.
class AdminBook(admin.ModelAdmin):
    model = Book
    fields = "__all__"

admin.site.register(Book, AdminBook)