from django.db import models
from django.conf import settings

# Create your models here.

class Movie(models.Model) :
    title = models.CharField(max_length=20) # 제목
    audience = models.IntegerField()    # 관객수
    relese_date = models.DateField()    # 개봉일
    genre = models.CharField(max_length=30) # 장르
    score = models.FloatField()         # 평점
    poster_url = models.TextField()     # 포스터 경로
    description = models.TextField()    # 줄거리
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)