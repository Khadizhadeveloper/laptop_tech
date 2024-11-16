from django.apps import AppConfig


class LaptopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'laptop'

    def ready(self):
        import laptop.signals
