from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Blog(models.Model):
    text = models.TextField()



class Pictures(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to="bloging")
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(120,60)])

    def __str__(self):
        return self.title