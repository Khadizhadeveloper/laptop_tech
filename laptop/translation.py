from modeltranslation.translator import TranslationOptions, translator
from .models import Laptop


class LaptopTranslationOptions(TranslationOptions):
    fields = ("name", "brand", "model", "price", "description", "image",
              "color", "stock", "processor", "ram", "storage", "screen_size", "release_date",
              "warranty_period", "rating", "is_active")

translator.register(Laptop, LaptopTranslationOptions)

