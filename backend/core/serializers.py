from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField



class LocationsSerializer(serializers.ModelSerializer):
    
    name = CharField(source="title", required=True)
    email = EmailField(required=True)
    message = CharField(source="description", required=True)
    latitude = CharField(source="description",required=True)
    longitude = CharField(source="description",required=True)
    
    class Meta:
        model = models.Locations
        fields = (
            'name',
            'email',
            'message',
            'latitude',
            'longitude'
        )