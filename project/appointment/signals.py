from django.core.mail import send_mail
from .models import Appointment
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_delete


@receiver(post_save, sender=Appointment)
def notify(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.client_name} {instance.date.strftime("%Y-%m-%d")}',
    else:
        subject = f' Appointment changed for {instance.client_name} {instance.date.strftime("%Y-%m-%d")}',
    send_mail(
        subject=subject,
        message=instance.message,
        from_email='',
        recipient_list=['ivangrigorev2817@gmail.com']
    )


@receiver(post_delete, sender=Appointment)
def notify_of_canceled(sender, instance, **kwargs):
    subject = f'{instance.client_name} has canceled his appointment!'
    send_mail(
        subject=subject,
        message=f'{instance.client_name} was canceled!',
        from_email='',
        recipient_list=['ivangrigorev2817@gmail.com']
    )
    print(subject)

