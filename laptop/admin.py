from django.contrib import admin

from laptop.models import Laptop

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    # Добавляем фильтры по полям
    list_filter = ['brand', 'price']

    # Добавляем нужные поля для отображения
    list_display = ['brand', 'price', 'ram', 'screen_size']

    # Настройка поиска по полям
    search_fields = ['brand']
# Register your models here.


