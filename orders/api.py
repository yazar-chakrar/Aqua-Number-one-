from .models import OrderLine, Order
from .serializer import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

#api v2
from rest_framework import generics

##  Order Lines
@api_view(['GET','POST'])
def order_lines_list_api(request):
    """
    Retrieveor Post a code food.
    """
    if request.method == 'GET':
        all_order_lines = OrderLine.objects.all()
        serializer = OrderLineSerializer(all_order_lines, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderLineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
    
@api_view(['GET','PUT','DELETE'])
def order_line_detail_api(request,o_id):
    """
    Retrieve, update or delete an order line.
    """
    try:
        order_line = OrderLine.objects.filter(order=o_id)
    except OrderLine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderLineSerializer(order_line, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderLineSerializer(order_line, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order_line.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##  Orders
@api_view(['GET','POST'])
def order_list_api(request):
    """
    Retrieveor Post an order.
    """
    if request.method == 'GET':
        all_orders = Order.objects.select_related('order_line').all()
        serializer = OrderSerializer(all_orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    
@api_view(['GET','PUT','DELETE'])
def order_detail_api(request,id):
    """
    Retrieve, update or delete a code food.
    """
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order_line = OrderLine.objects.filter(order=o_id)
        order_line.delete()
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##  Orders with their Order Lines    
@api_view(['GET'])
def order_with_lines_list_api(request):
    """
    Retrieveor Post a code food.
    """
    if request.method == 'GET':
        all_orders = Order.objects.all()
        serializer = OrdersOlListsSerializer(all_orders, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def order_with_lines_detail_api(request, id):
    """
    Retrieveor Post a code food.
    """
    if request.method == 'GET':
        order = Order.objects.get(id=id)
        serializer = OrdersOlListsSerializer(order)
        return Response(serializer.data)


#############################################
                    #Generics Views v2Api
#############################################                
                    
class OrderLinesListApi(generics.ListCreateAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    
    
class OrderLineDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    lookup_field = 'order'
    
    
    
class OrderListApi(generics.ListCreateAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderSerializer
    
    
class OrderListApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'