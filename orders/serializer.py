from rest_framework import serializers
from .models import Order, OrderLine
from foods.models import Food
from foods.serializer import FoodSerializer

#from ..foods.models import Food
#from ..foods.serializer import *


# Serializers define the API representation.
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'constumer', 'created_at']


class OrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = ['id', 'order', 'food', 'quant', 'line_price']

    line_price = serializers.SerializerMethodField(method_name='cal_line_price')
    
    def cal_line_price(self, order_line:OrderLine):
        return order_line.food.price * order_line.quant
    
    ''' order = serializers.HyperlinkedRelatedField(
        queryset = Order.objects.all(),
        view_name = 'order-detail'
        
    ) '''
 
        
class OrdersOlListsSerializer(OrderSerializer):
    order_lines = serializers.SerializerMethodField()
    totale_price = serializers.SerializerMethodField()

    def get_order_lines(self, instance):
        serializer = []
        for ol in instance.order_of_line.all() :
            serializer.append({'line' : OrderLineSerializer(ol).data, 'line_price' :ol.quant*ol.food.price})
            
        p = OrderLineSerializer(instance.order_of_line.all(), many=True).data 
        return serializer
    
    def get_totale_price(self, instance):
        price = 0
        for ol in instance.order_of_line.all() :
            price = price + ol.quant*ol.food.price
        return price

    class Meta(OrderSerializer.Meta):
        fields = (
            'constumer',
            'location',
            'postal_code',
            'order_lines',
            'created_at',
            'totale_price'
        )