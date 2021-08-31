from django.shortcuts import render

from .models import Order, OrderMenu, Payment
from .serializers import OrderSerializer, OrderMenuSerializer, PaymentSerializer
from rest_framework import viewsets


class Order_view_set(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class Order_menu_view_set(viewsets.ModelViewSet):
    queryset = OrderMenu.objects.all()
    serializer_class = OrderMenuSerializer


class Payment_view_set(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
