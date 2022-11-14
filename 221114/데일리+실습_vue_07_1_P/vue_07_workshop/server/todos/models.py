from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
