
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="memos"
urlpatterns = [
    path('',views.index,name="index"),
    path('create/',views.create,name='create'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/delete',views.delete,name='delete'),
    path('<int:pk>/update',views.update,name='update'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
