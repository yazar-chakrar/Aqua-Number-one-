from unicodedata import category
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import Food

#api v2
from rest_framework import generics


@api_view(['GET','POST'])
def food_list_api(request):
    if request.method == 'GET':
        all_foods = Food.objects.all()
        serializer = FoodSerializer(all_foods, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def food_category_api(request, cat):
    if request.method == 'GET':
        food_detail = Food.objects.filter(category=cat)
        serializer = FoodSerializer(food_detail, many=True)
        return Response(serializer.data)


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