from django.urls import path

from . import api

app_name='orders'
urlpatterns = [
    ##Api urls
        #Order Lines
    path('api/order_lines', api.order_lines_list_api , name = 'order_lines_list_api'),
    path('api/order_lines/<int:o_id>', api.order_line_detail_api , name = 'order_line_detail_api'),
        
        #Orders
    path('api/orders', api.order_list_api , name = 'order_list_api'),
    path('api/orders/<int:id>', api.order_detail_api , name = 'order_detail_api'),
    
        #Orders
    path('api/orders_w_lines', api.order_with_lines_list_api , name = 'order_with_lines_list_api'),
    path('api/orders_w_lines/<int:id>', api.order_with_lines_detail_api , name = 'order_with_lines_detail_api'),
    
]