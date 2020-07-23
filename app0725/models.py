from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Blog(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.title


class Pictures(models.Model):
    text=models.TextField()
    image = models.ImageField(upload_to="bloging")
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(120,60)])
