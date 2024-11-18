from modeltranslation.translator import TranslationOptions, translator
from .models import Laptop


class LaptopTranslationOptions(TranslationOptions):
    fields = ( "description","color",)

translator.register(Laptop, LaptopTranslationOptions)

