from rest_framework import serializers
from .models import CustomerDetails, CustomerFileMapping

class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name','mobile_no')
        model = CustomerDetails
