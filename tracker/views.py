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


class UserProfile(generics.RetrieveUpdateAPIView):
    def get_queryset(self):
        queryset = Profile.objects.filter(user_id=self.kwargs["pk"])
        return queryset

    serializer_class = ProfileSerializer

    def put(self, request, *args, **kwargs):
        profile = Profile.objects.get(user_id=self.kwargs["pk"])
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


