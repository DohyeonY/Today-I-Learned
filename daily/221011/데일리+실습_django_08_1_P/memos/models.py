
from django.db import models
from django.conf import settings
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField

# Create your models here.
class Memo(models.Model):

    summary = models.CharField(max_length=20)
    memo = models.TextField()
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200,200)],
        format='JPEG',
        options={'quality': 80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
