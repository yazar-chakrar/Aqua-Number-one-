from unicodedata import category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import Food

#api v2
from rest_framework import generics


@api_view(['GET'])
def food_list_api(request):
    all_foods = Food.objects.all()
    data = FoodSerializer(all_foods, many=True).data
    context = {'food-list':data}
    return Response(context)


@api_view(['GET'])
def food_category_api(request, cat):
    food_detail = Food.objects.filter(category=cat)
    data = FoodSerializer(food_detail, many=True).data
    context = {'food-list':data}
    return Response(context)


#############################################
                    #Generics Views v2Api
#############################################                
                    
class FoodListApi(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    
    
class FoodDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    lookup_field = 'id'