from .models import OrderLine, Order
from django.db.models import Count
from django.shortcuts import get_object_or_404
from .serializer import *
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
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
        all_order_lines = OrderLine.objects.select_related('order').all()
        serializer = OrderLineSerializer(all_order_lines, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderLineSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    
@api_view(['GET','PUT','DELETE'])
def order_line_detail_api(request,pk):
    """
    Retrieve, update or delete an order line.
    """
    try:
        order_line = OrderLine.objects.get(id=pk)
    except OrderLine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderLineSerializer(order_line)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderLineSerializer(order_line, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        order_line.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def order_lines_detail_by_order_api(request,o_pk):
    """
    Retrieve, update or delete an order line.
    """
    try:
        order_line = OrderLine.objects.filter(order=o_pk)
    except OrderLine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderLineSerializer(order_line, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderLineSerializer(order_line, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

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
        all_orders = Order.objects.annotate(lines_count=Count('order_of_line')).all()
        serializer = OrderSerializer(all_orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def order_detail_api(request,pk):
    """
    Retrieve, update or delete a code food.
    """
    try:
        order = Order.objects.annotate(lines_count=Count('order_of_line')).get(id=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
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
    lookup_field = 'id'
   
    
class OrderLineDetailByOrderApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    lookup_field = 'order'
    
     
class OrderListApi(generics.ListCreateAPIView):
    queryset = Order.objects.annotate(lines_count=Count('order_of_line')).all()
    serializer_class = OrderSerializer
    
    
class OrderDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.annotate(lines_count=Count('order_of_line')).all()
    serializer_class = OrderSerializer
    
    def delete(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        if order.order_of_line.count() > 0 :
            return Response({'Err':'Err Inh'})
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
#############################################
                    #ViewSets v3Api
############################################# 

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.annotate(lines_count=Count('order_of_line')).all()
    serializer_class = OrderSerializer
    
    def destroy(self, request, *args, **kwargs):
        if OrderLine.objects.filter(order_id=kwargs['pk']).count() > 0 :
            return Response({'Err':'Err Inh'})
        return super().destroy(request, *args, **kwargs)
    
    
class OrderLineViewSet(ModelViewSet):
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer
    
    def destroy(self, request, *args, **kwargs):
        if OrderLine.objects.filter(order_id=kwargs['pk']).count() > 0 :
            return Response({'Err':'Err Inh'})
        return super().destroy(request, *args, **kwargs)