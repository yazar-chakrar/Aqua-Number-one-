from django.urls import path

from . import views, api

app_name='foods'
urlpatterns = [
    ##Api urls
    path('api/foods', api.food_list_api , name = 'food_list_api'),
    path('api/foods/<int:pk>', api.food_detail_api , name = 'food-detail'),
    
    ##Api Class Based View
    path('api/v2/foods', api.FoodListApi.as_view() , name = 'food_list_v2_api'),
    path('api/v2/foods/<int:id>', api.FoodDetailApi.as_view() , name = 'food_detail_v2_api'),
    
    
    
    #Templates urls
    path('create_food', views.create_food , name = 'create_food'),
]