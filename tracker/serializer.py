from rest_framework import serializers
from .models import Profile, Device, GPSCoordinate, SecondaryCircuit


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'bio', 'location', 'profile_pic')



