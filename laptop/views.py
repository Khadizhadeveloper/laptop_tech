from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from .models import Laptop, Order
from .serializers import LaptopSerializer, OrderSerializer
from .permissions import IsAdminUser

class LaptopListCreate(generics.ListCreateAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    permission_classes = [IsAdminUser]


class LaptopDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    permission_classes = [IsAdminUser]


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]
