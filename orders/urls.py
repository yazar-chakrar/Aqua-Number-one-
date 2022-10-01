from django.urls import path

from . import api

app_name='orders'
urlpatterns = [
    ##Api urls
        #Order Lines
    path('api/order_lines', api.order_lines_list_api , name = 'order_lines-list'),
    path('api/order_lines/<int:pk>', api.order_line_detail_api , name = 'order_line-detail'),
    path('api/order-order_lines/<int:o_pk>', api.order_lines_detail_by_order_api , name = 'order-order_line-detail'),
        
        #Orders
    path('api/orders', api.order_list_api , name = 'order-list'),
    path('api/orders/<int:pk>', api.order_detail_api , name = 'order-detail_'),
    
        #Orders with ordered lines and price 
        #Just to learn customizing and serializing
        #This process should effectued on front end
    path('api/orders_w_lines', api.order_with_lines_list_api , name = 'order_with_lines-list'),
    path('api/orders_w_lines/<int:id>', api.order_with_lines_detail_api , name = 'order_with_lines-detail'),
    
    
    
    #Api v2 using CBV
        #Order Lines
    path('api/v2/order_lines', api.OrderLinesListApi.as_view() , name = 'order_lines-list_v2'),
    path('api/v2/order_lines/<int:o_id>', api.OrderLineDetailApi.as_view() , name = 'order_line-detail_v2'),
    path('api/v2/order-order_lines/<int:o_id>', api.OrderLineDetailByOrderApi.as_view() , name = 'order_line_detail_v2'),
        
        #Orders
    path('api/v2/orders', api.OrderListApi.as_view() , name = 'order-list_v2'),
    path('api/v2/orders/<int:pk>', api.OrderListApi.as_view() , name = 'order-detail'),
    
]