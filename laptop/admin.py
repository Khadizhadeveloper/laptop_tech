from django.contrib import admin
from .models import Laptop

class LaptopAdmin(admin.ModelAdmin):
    readonly_fields = ('total_rating', 'rating_count')  # исключаем поля из админки

admin.site.register(Laptop,LaptopAdmin)