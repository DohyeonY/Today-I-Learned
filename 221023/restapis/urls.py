from django.urls import path
from . import views

urlpatterns = [
    path('html/', views.apilist),
]
