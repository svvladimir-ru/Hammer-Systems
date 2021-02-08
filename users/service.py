from django.core.mail import send_mail
import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def email(message, message2):
    messages = f'Код регистрации: \n{message2}'
    send_mail(
        'hammer',
        messages,
        f'{message}',  # почта куда
        [f'{message}'],  # Это поле Кому:
        fail_silently=False,
    )
