from modeltranslation.translator import register, TranslationOptions
from .models import Laptop

@register(Laptop)
class LaptopTranslationOptions(TranslationOptions):
    fields = ('name', 'brand', 'model', 'description', 'color')
