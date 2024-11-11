from modeltranslation.translator import TranslationOptions, register

from .models import Laptop


@register(Laptop)
class LaptopTranslationOptions(TranslationOptions):
    fields = ("description",
              "color")
