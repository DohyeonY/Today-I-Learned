from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_pk>/', views.book_detail, name='book_detail'),
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    path('books/<int:book_pk>/comments/', views.comment_create, name='comment_create'),
]
