from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        id = self.pk
        title = self.title
        content = self.content
        return f'{id}번글 - {title} : {content}'