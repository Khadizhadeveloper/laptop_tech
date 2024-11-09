from django.db import models
from django.utils.translation import gettext_lazy as _

class Laptop(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    model = models.CharField(max_length=255, verbose_name=_('Model'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='laptops/', verbose_name=_('Image'))
    color = models.CharField(max_length=255, verbose_name=_('Color'))
    processor = models.CharField(max_length=255, verbose_name=_('Processor'))
    ram = models.IntegerField(verbose_name=_('RAM'))
    storage = models.IntegerField(verbose_name=_('Storage'))
    screen_size = models.DecimalField(max_digits=3, decimal_places=1, verbose_name=_('Screen size'))
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, verbose_name=_('Rating'), blank=True)
    stock = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model}"
