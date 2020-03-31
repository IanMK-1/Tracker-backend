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
        try:
            queryset = Profile.objects.filter(user_id=self.kwargs["pk"])
        except ObjectDoesNotExist:
            return Response({"Profile does not exist"}, status=status.HTTP_400_BAD_REQUEST)

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


class CreateDevice(generics.ListCreateAPIView):
    def get_queryset(self):
        try:
            queryset = Device.objects.filter(user_id=self.kwargs["pk"])
        except ObjectDoesNotExist:
            return Response({"Device does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        return queryset

    serializer_class = DeviceSerializer

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(pk=self.kwargs["pk"])
        except ObjectDoesNotExist:
            return Response({"User does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        device = Device(user=user)
        serializer = DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceList(generics.ListAPIView):
    def get_queryset(self):
        try:
            devices = Device.objects.filter(user_id=self.kwargs["pk"])
        except ObjectDoesNotExist:
            return Response({"Device does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        return devices

    serializer_class = DeviceSerializer


class CreateGPS(generics.ListCreateAPIView):
    def get_queryset(self):
        try:
            gps = GPSCoordinate.objects.filter(device_device_identifier=self.kwargs["device_identifier"])
        except ObjectDoesNotExist:
            return Response({"Device does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        return gps

    serializer_class = GPSSerializer

    def post(self, request, *args, **kwargs):
        try:
            device = Device.objects.get(device_identifier=self.kwargs["device_identifier"])
        except ObjectDoesNotExist:
            return Response({"Device does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        command = self.kwargs["command"]
        longitude = self.kwargs["longitude"]
        latitude = self.kwargs["latitude"]
        data = {"device_identifier": self.kwargs["device_identifier"], "command": command, "longitude": longitude,
                "latitude": latitude, "device": device.id}
        serializer = GPSSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)