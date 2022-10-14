from configparser import MAX_INTERPOLATION_DEPTH
from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings

# Create your models here.

class Movie(models.Model) :
    title = models.CharField(max_length=10)
    description = models.TextField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.CharField(max_length=200)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)