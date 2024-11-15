from django.contrib import admin

from laptop.models import Laptop, Order


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    # Добавляем фильтры по полям
    list_filter = ['brand', 'price']

    # Добавляем нужные поля для отображения
    list_display = ['brand', 'price', 'ram', 'screen_size']

    # Настройка поиска по полям
    search_fields = ['brand']
# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email', 'laptop', 'created_at']
    search_fields = ['name', 'laptop']
    list_filter = ['created_at', 'laptop']


