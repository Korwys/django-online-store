import smtplib

from django.urls import reverse

from mainapp import settings
from mainapp.settings import env


def send_verification_email(user):
    """Отправляет письмо юзеру на указанный им в форме email для подтверждения регистрации"""

    sender = env('GMAIL_USER_NAME')
    sender_password = env('GMAIL_USER_PASSWORD')

    email_verify_link = reverse('auth:confirm_new_user_registration', args=[user.email, user.activation_key])

    message = f'Для подтверждения учетной записи {user.username} на портале {settings.DOMAIN_NAME} ' \
              f'перейдите по ссылке:{settings.DOMAIN_NAME}{email_verify_link}'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, sender_password)
        server.sendmail(sender, user.email, message.encode('utf-8'))
    except Exception as ex:
        return f"{ex} Что-то не так! Проверь логин/пароль."
