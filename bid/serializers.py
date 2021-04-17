from rest_framework import serializers

from .models import Bid, Street, Area, Location
from django.contrib.auth.models import User


class BidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bid
        fields='__all__'

class StreetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Street
        fields='__all__'

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Area
        fields='__all__'

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Location
        fields='__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']