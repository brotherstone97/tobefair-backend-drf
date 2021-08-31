from rest_framework import serializers
from .models import Order,OrderMenu,Payment

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMenu
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'