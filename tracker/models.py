from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    profile_pic = CloudinaryField('image', blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __repr__(self):
        return self.user


class Device(models.Model):
    device_identifier = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    description = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.device_identifier


class GPSCoordinate(models.Model):
    device_identifier = models.CharField(max_length=30)
    command = models.CharField(max_length=30)
    longitude = models.FloatField()
    latitude = models.FloatField()
    received_on = models.DateTimeField(auto_now_add=True)

    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.device_identifier


class SecondaryCircuit(models.Model):
    device_identifier = models.CharField(max_length=30)
    command = models.CharField(max_length=30)
    message = models.TextField()
    received_on = models.DateTimeField(auto_now_add=True)

    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.device_identifier
