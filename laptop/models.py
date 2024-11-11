from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    class Meta:
        abstract = True  # Абстрактная модель, не будет создавать таблицу в БД

    def __str__(self):
        return self.name
class Laptop(Product):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    brand = models.CharField(max_length=255, verbose_name=_('Brand'))
    model = models.CharField(max_length=255, verbose_name=_('Model'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='laptops/', verbose_name=_('Image'))
    color = models.CharField(max_length=255, verbose_name=_('Color'))
    processor = models.CharField(max_length=255, verbose_name=_('Processor'))
    ram = models.IntegerField(verbose_name=_('RAM'))
    storage = models.IntegerField(verbose_name=_('Storage'))
    screen_size = models.DecimalField(max_digits=3, decimal_places=1, verbose_name=_('Screen size'))
    stock = models.BooleanField(default=False)

    total_rating = models.PositiveIntegerField(default=0)  # Сумма всех оценок
    rating_count = models.PositiveIntegerField(default=0)  # Количество голосов

    @property
    def average_rating(self):
        return self.total_rating / self.rating_count if self.rating_count > 0 else 0

    def __str__(self):
        return f"{self.brand} {self.model}"


