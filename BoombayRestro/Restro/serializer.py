from rest_framework import serializers
from Restro.models import category

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ['title']
        
