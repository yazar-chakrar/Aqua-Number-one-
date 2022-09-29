from unicodedata import category
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import Book, BookCategory

#api v2
from rest_framework import generics

@api_view(['GET','POST'])
def book_list_api(request):
    """
    Retrieveor Post a code Book.
    """
    if request.method == 'GET':
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def book_detail_api(request, id):  
    """
    Retrieve, update or delete a code food.
    """
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def book_cat_list_api(request):
    """
    Retrieveor Post a code Book.
    """
    if request.method == 'GET':
        all_book_cats = Book.objects.all()
        serializer = BookCategorySerializer(all_book_cats, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def book_cat_detail_api(request, id):  
    """
    Retrieve, update or delete a code food.
    """
    try:
        book_cat = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookCategorySerializer(book_cat)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookCategorySerializer(book_cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book_cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#############################################
                    #Generics Views v2Api
#############################################                
                    
class BookListApi(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'
    
    
class BookCatListApi(generics.ListCreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    
    
class BookCatDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    lookup_field = 'id'