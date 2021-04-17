from rest_framework import serializers

from .models import Driver, CarBrand, Car
from django.contrib.auth.models import User


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = (
            'have_car',
            'callsign',
            'lastname',
            'date_of_birth',
            'work_experience'
        )

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Car
        fields='__all__'

class CarBrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=CarBrand
        fields='__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']