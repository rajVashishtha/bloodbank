from rest_framework import serializers
from .models import State, BloodBank, BloodGroup, Size, BloodBag

class BloodBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBank
        fields = (
            'name',
            'email',
            'password',
            'address',
            'pincode',
            'state',
            'city',
            'latitude',
            'longitude'    
        )


class DynamicSerializer(BloodBankSerializer):
    class Meta:
        model = BloodBank
        fields = (
            'name',
            'address',
            'pincode',
            'state',
            'city',
            'latitude',
            'longitude' 
        )        


