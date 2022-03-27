from rest_framework import serializers
from .models import OrdersDetails, FileDetails

class OrdersDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('customer_id','type','description')
        model = OrdersDetails


class CustomerOrderSerailizer(serializers.Serializer):
    name = serializers.CharField()
    mobile_no = serializers.IntegerField()
    type = serializers.CharField(max_length=220)
    description = serializers.CharField(max_length=220)


class OrderListSerailizer(serializers.ModelSerializer):
    name = serializers.CharField()
    mobile_no = serializers.IntegerField()
    class Meta:
        fields = ('order_id','name','mobile_no','customer_id','type','description','created_date')
        model = OrdersDetails