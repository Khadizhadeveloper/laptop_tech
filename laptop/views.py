from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from .models import Laptop
from .serializers import LaptopSerializer
from .permissions import IsAdminUser

class LaptopListCreate(generics.ListCreateAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    permission_classes = [IsAdminUser]


class LaptopDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    permission_classes = [IsAdminUser]






