from mainapp.celery import app
from .services.email import send_verification_email


@app.task
def send_activation_link_on_email(email, activation_key, username):
    """ Вызывает функцию которая в свою очередь отправляет емейл для активации учетной записи"""
    send_verification_email(email, activation_key, username)
