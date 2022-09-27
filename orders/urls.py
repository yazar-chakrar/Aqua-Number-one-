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
    
        #Orders with ordered lines and price 
        #Just to learn customizing and serializing
        #This process should effectued on front end
    path('api/orders_w_lines', api.order_with_lines_list_api , name = 'order_with_lines_list_api'),
    path('api/orders_w_lines/<int:id>', api.order_with_lines_detail_api , name = 'order_with_lines_detail_api'),
    
    
    
    #Api v2 using CBV
        #Order Lines
    path('api/v2/order_lines', api.OrderLinesListApi.as_view() , name = 'order_lines_list_api'),
    path('api/v2/order_lines/<int:o_id>', api.OrderLineDetailApi.as_view() , name = 'order_line_detail_api'),
        
        #Orders
    path('api/v2/orders', api.OrderListApi.as_view() , name = 'order_list_api'),
    path('api/v2/orders/<int:id>', api.OrderListApi.as_view() , name = 'order_detail_api'),
    
]