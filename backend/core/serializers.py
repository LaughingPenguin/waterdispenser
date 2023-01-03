from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField



class ContactSerializer(serializers.ModelSerializer):
    
    name = CharField(source="title", required=True)
    email = EmailField(required=True)
    message = CharField(source="description", required=True)
    longitude = CharField(source="place",required=True)
    latitude = CharField(source="place",required=True)
    
    class Meta:
        model = models.Locations
        fields = (
            'name',
            'email',
            'message',
            'longitude',
            'latitude'
        )