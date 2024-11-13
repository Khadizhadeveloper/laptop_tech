# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Order
from django.conf import settings

@receiver(post_save, sender=Order)
def send_order_notification(sender, instance, created, **kwargs):
    if created:  # Только при создании нового заказа
        subject = f"Новый заказ от {instance.name}"
        message = (
            f"Заказ оформлен от {instance.name} на ноутбук {instance.laptop}.\n"
            f"Контактная информация:\n"
            f"Телефон: {instance.phone}\n"
            f"Email: {instance.email}"
        )
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,  # От кого (уже настроено в settings.py)
            ['blossomblessed9@gmail.com'],  # Замените на почту вашей компании
        )
