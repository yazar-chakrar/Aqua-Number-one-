from dataclasses import field
from pyexpat import model
from django import forms
from .models import Food

class CreateFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["category","title","disc", "image", "price", "old_price", "is_avaible"]
            