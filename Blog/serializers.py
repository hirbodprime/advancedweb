from dataclasses import fields
from rest_framework import serializers
from .models import blogmodel

# class blogserializer(serializers.ModelSerializer):
#     class Meta:
#         model = blogmodel
#         fields = ['wrtier' ,'title' ,'body','date']



from rest_framework import serializers
from .models import blogmodel, contactModel

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = blogmodel
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contactModel
        fields = '__all__'
