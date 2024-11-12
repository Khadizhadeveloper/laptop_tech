from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .models import Laptop, Order

class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = ['name', 'description', 'price']
        extra_kwargs = {
            'name': {'help_text': _("Название ноутбука")},
            'description': {'help_text': _("Описание ноутбука")},
        }

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'name', 'email', 'phone', 'laptop', 'created_at']