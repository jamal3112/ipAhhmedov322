from django.shortcuts import render
from rest_framework import viewsets

from .serializers import DriverSerializer, CarBrandSerializer, CarSerializer, UserSerializer
from .models import CarBrand, Driver, Car
from django.contrib.auth.models import User

# Create your views here.


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class CarBrandSet(viewsets.ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
