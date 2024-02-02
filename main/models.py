from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField(max_length=200)
    image = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.title

class ServiceDetails(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE)
    additional_info = models.TextField(max_length=500)
    
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 100}
    )
    
    def __str__(self):
        return f"Details for {self.service.title}"

class Image(models.Model):
    image = models.ImageField(upload_to='media')
    alt_text = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(150, 150)],
        format='JPEG',
        options={'quality': 100}
    )


    def __str__(self):
        return self.title

class Trainer(models.Model):
    name = models.CharField(max_length=50)
    expertise = models.TextField(max_length=200)
    description = models.TextField(max_length=200)
    image = models.ImageField(blank=True, null=True, upload_to='media')

    def __str__(self):
        return self.name

