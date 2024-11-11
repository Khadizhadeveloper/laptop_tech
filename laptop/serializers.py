from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .models import Laptop

class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'
        extra_kwargs = {
            'title': {'help_text': _("Название ноутбука")},
            'description': {'help_text': _("Описание ноутбука")},
        }

