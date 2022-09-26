from unicodedata import category
from django.contrib import admin

# Register your models here.
from .models import Food, Category

admin.site.register(Category)
admin.site.register(Food)