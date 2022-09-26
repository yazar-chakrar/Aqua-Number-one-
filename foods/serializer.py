from rest_framework import serializers
from .models import Food


# Serializers define the API representation.
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        #fields = ["id","category","title","disc", "image", "price", "old_price", "is_avaible"]
        fields = "__all__"