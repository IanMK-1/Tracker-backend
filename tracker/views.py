from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView

from .models import Profile, GPSCoordinate, Device, SecondaryCircuit
from .serializer import ProfileSerializer, DeviceSerializer, GPSSerializer, SecondaryCircuitSerializer, UserSerializer


# Create your views here.
class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserProfile(generics.ListAPIView):
    def get_queryset(self):
        queryset = Profile.objects.filter(user_id=self.kwargs["pk"])
        return queryset

    serializer_class = ProfileSerializer


class UpdateUserProfile(generics.UpdateAPIView):
    def put(self, request, *args, **kwargs):
        profile = Profile.objects.get(user_id=self.kwargs["pk"])
        user = User.objects.filter(pk=self.kwargs["pk"])
        name = request.data.get("name")
        bio = request.data.get("bio")
        location = request.data.get("location")
        profile_pic = request.data.get("profile_pic")
        data = {"name": name, "bio": bio, "location": location, "profile_pic": profile_pic, "user": user}
        serializer = ProfileSerializer(profile, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateDevice(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(pk=self.kwargs["pk"])
        device_identifier = request.data.get("device_identifier")
        name = request.data.get("name")
        description = request.data.get("description")
        data = {"device_identifier": device_identifier, "name": name, "description": description, "user": user}
        serializer = DeviceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
