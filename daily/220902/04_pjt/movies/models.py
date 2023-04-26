from distutils import text_file
from pyexpat import model
from django.db import models
from datetime import datetime
# Create your models here.

class Movie(models.Model) :
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField(null = True, blank = True)
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
    
