from django.urls import path

from . import views, api

app_name='books'

urlpatterns = [
        #v2
    path('api/books', api.book_list_api , name = 'book_list_api'),
    path('api/book_detail/<int:id>', api.book_detail_api , name = 'book_detail_api'),
    path('api/book_cats', api.book_cat_list_api , name = 'book_cat_list_api'),
    path('api/book_cats/<int:id>', api.book_cat_detail_api , name = 'book_cat_detail_api'),
    
    
        ##Api Class Based View
    path('api/v2/books', api.BookListApi.as_view() , name = 'book_list_v2_api'),
    path('api/v2/books/<int:id>', api.BookDetailApi.as_view() , name = 'book_detail_v2_api'),
    path('api/v2/book_cats', api.BookCatListApi.as_view() , name = 'food_list_v2_api'),
    path('api/v2/book_cats/<int:id>', api.BookCatDetailApi.as_view() , name = 'food_detail_v2_api'),
        
]