from mainapp.celery import app
from .services.email import send_verification_email


@app.task
def send_activation_link_on_email(email, activation_key, username):
    send_verification_email(email, activation_key, username)
