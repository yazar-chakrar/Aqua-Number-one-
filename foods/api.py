from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import Food


@api_view(['GET'])
def food_list_api(request):
    all_foods = Food.objects.all()
    data = FoodSerializer(all_foods, many=True).data
    context = {'data':data}
    return Response(context)