from django.urls import path
from ..pages import views

urlpatterns = [
    path('pages-index/', views.index),
]