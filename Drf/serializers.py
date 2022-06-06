from dataclasses import fields
from rest_framework import serializers
from .models import blogmodel

class blogserializer(serializers.ModelSerializer):
    class Meta:
        model = blogmodel
        fields = ['wrtier' ,'title' ,'body','date']