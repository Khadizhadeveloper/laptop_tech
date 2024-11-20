# laptop/tasks.py
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_order_email(order_id, name, email, phone, laptop):
    subject = f"Новый заказ от {name}"
    message = (
        f"Информация о заказе:\n"
        f"Имя клиента: {name}\n"
        f"Email клиента: {email}\n"
        f"Телефон клиента: {phone}\n"
        f"Ноутбук: {laptop}\n"
    )
    send_mail(
        subject,
        message,
        'blossomblessed9@gmail.com',  # Замените на вашу почту
        ['khadizha.asangazieva@kstu.kg'],  # Почта, куда отправлять уведомление
    )
