from django.urls import path

from . import views, api

app_name='foods'
urlpatterns = [
    ##Api urls
    path('food_list_api', api.food_list_api , name = 'food_list_api'),
    
    
    
    #Templates urls
    path('new_food', views.create_food , name = 'create_food'),
]