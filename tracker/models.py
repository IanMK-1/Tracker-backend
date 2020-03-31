from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    profile_pic = CloudinaryField('image', blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
