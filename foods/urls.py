from django.urls import path

from . import views

app_name='foods'
urlpatterns = [
    path('new_food', views.create_food , name = 'create_food'),
]