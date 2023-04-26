from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        id = self.pk
        title = self.title
        genre = self.genre
        return f'{id}번글 - {title} : ({genre})'