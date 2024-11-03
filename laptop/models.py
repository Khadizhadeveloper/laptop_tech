from django.db import models
from django.utils.translation import gettext_lazy as _

class Laptop(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    brand = models.CharField(max_length=255, verbose_name=_('Brand'))
    model = models.CharField(max_length=255, verbose_name=_('Model'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='laptops/', verbose_name=_('Image'))
    color = models.CharField(max_length=255, verbose_name=_('Color'))
    stock = models.IntegerField(verbose_name=_('Stock'))
    processor = models.CharField(max_length=255, verbose_name=_('Processor'))
    ram = models.IntegerField(verbose_name=_('RAM'))
    storage = models.IntegerField(verbose_name=_('Storage'))
    screen_size = models.DecimalField(max_digits=3, decimal_places=1, verbose_name=_('Screen size'))
    release_date = models.DateField(verbose_name=_('Release date'))
    warranty_period = models.DateField(verbose_name=_('Warranty period'))
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, verbose_name=_('Rating'))
    is_active = models.BooleanField(default=True, verbose_name=_('Active'))

    def __str__(self):
        return f"{self.brand} {self.model}"
