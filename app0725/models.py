from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Pictures(models.Model):
    title = models.CharField(max_length=100, default="title")
    text = models.TextField()
    image = models.ImageField(upload_to="bloging")
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(240,150)])

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:100]