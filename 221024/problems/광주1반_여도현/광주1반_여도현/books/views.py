from logging import exception
from msilib.schema import ServiceInstall
from my_api.settings import ALLOWED_HOSTS
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import BookListSerializer, BookSerializer, CommentSerializer
from .models import Book, Comment

@api_view(['GET', 'POST'])
def book_list(request):
    # Q 1.
    if request.method == 'GET' :
        books = get_list_or_404(Book)
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    # Q 2.
    elif request.method == 'POST' :
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'DELETE', 'PUT'])
def book_detail(request, book_pk):
    # Q 3.
    books = get_object_or_404(Book, pk=book_pk)
    if request.method == 'GET' :
        serializer = BookSerializer(books)
        return Response(serializer.data)
    # Q 4.
    elif request.method == 'DELETE' :
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # Q 5.
    elif request.method == 'PUT' :
        serializer = BookSerializer(books, data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    # Q 7.
    if request.method == 'GET' :
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, book_pk):
    # Q 8.
    if request.method == 'POST' :
        book= get_object_or_404(Book, pk = book_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save(book=book)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'DELETE'])
def comment_detail(request, comment_pk):
    # Q 9.
    comments = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET' :
        serializer = CommentSerializer(comments)
        return Response(serializer.data)
    # Q 10.
    elif request.method == 'DELETE' :
        comments.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

