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


