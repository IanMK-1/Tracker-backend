from rest_framework import serializers
from .models import Profile, Device, GPSCoordinate, SecondaryCircuit


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'bio', 'location', 'profile_pic')


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('device_identifier', 'name', 'description')


class GPSSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSCoordinate
        fields = '__all__'


