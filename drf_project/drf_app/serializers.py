from rest_framework import serializers
from .models import PhoneNumber, SpamNumber

class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['number', 'name']
        
class SpamNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamNumber
        fields = ['number']
