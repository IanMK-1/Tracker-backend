from django.contrib import admin
from .models import Profile, Device, GPSCoordinate, SecondaryCircuit

# Register your models here.
admin.site.register(Profile)
admin.site.register(Device)
admin.site.register(GPSCoordinate)
admin.site.register(SecondaryCircuit)
