from django.contrib import admin

# Register your models here.
from .models import Book, BookCategory

admin.site.register(BookCategory)
admin.site.register(Book)