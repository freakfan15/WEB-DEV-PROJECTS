from django.contrib.admin.sites import DefaultAdminSite
from django.db import models
from datetime import datetime

# Create your models here.
class Youtuber(models.Model):

    crew_choices = (
        ('solo', 'solo'),
        ('small', 'small'),
        ('solo', 'solo'),
    )

    camera_choices = (
        ('sony', 'sony'),
        ('canon', 'canon'),
        ('nikon', 'nikon'),
        ('panasonic', 'panasonic'),
        ('red', 'red'),
        ('fuji', 'fuji'),
        ('other', 'other'),
    )

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to = 'media/ytubers/%Y/%m/')
    video_url = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField(max_length=255)
    height = models.IntegerField(max_length=255)
    crew = models.CharField(max_length=255)
    camera_type = models.CharField(max_length=255)
    subs_count = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    category = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=datetime.now, blank=True)