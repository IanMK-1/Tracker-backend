from rest_framework import serializers
from .models import Profile, Device, GPSCoordinate, SecondaryCircuit
from django.contrib.auth.models import User


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


class SecondaryCircuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondaryCircuit
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
