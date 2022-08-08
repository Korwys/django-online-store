import logging
import smtplib

from django.urls import reverse

from mainapp import settings
from mainapp.settings import env

logger = logging.getLogger('django_logger')


def send_verification_email(user):
    """Отправляет письмо юзеру на указанный им в форме email для подтверждения регистрации"""

    sender = env('GMAIL_USER_NAME')
    sender_password = env('GMAIL_USER_PASSWORD')

    email_verify_link = reverse('auth:confirm_new_user_registration', args=[user.email, user.activation_key])

    message = f'Для подтверждения учетной записи {user.username} на портале {settings.DOMAIN_NAME} ' \
              f'перейдите по ссылке:{settings.DOMAIN_NAME}{email_verify_link}'
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
    except ConnectionError as e:
        logging.error('Проблема с подключением к gmail')

    try:
        server.login(sender, sender_password)
        server.sendmail(sender, user.email, message.encode('utf-8'))
    except ValueError as e:
        logging.error(e)
