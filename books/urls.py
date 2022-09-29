from django.urls import path

from . import views, api

app_name='books'

urlpatterns = [
        #v2
    path('api/books', api.book_list_api , name = 'book_list_api'),
    path('api/book_detail/<int:id>', api.book_detail_api , name = 'book_detail_api'),
    path('api/book_cats', api.book_cat_list_api , name = 'book_cat_list_api'),
    path('api/book_cats/<int:id>', api.book_cat_detail_api , name = 'book_cat_detail_api'),
    
]