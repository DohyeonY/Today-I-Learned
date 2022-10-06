from secrets import choice
from django.db import models



# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    issue_a = models.CharField(max_length=100)
    issue_b = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.BooleanField()
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
