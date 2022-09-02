from django.contrib import admin
from .models import Article
# Register your models here.

class table(admin.ModelAdmin) :
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')

admin.site.register(Article, table)