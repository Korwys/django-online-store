from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class User(AbstractUser):
    """Модель описывает пользователя"""

    avatar = models.ImageField(
        upload_to='user_avatar',
        blank=True,
    )

    is_active = models.BooleanField(
        verbose_name='Статус',
        default=True,
    )

    created_at = models.DateTimeField(
        verbose_name='Последнее измение',
        auto_now=True

    )

    activation_key = models.CharField(
        max_length=128,
        verbose_name='Ключ активации',
        blank=True
    )

    activation_key_expires = models.DateTimeField(
        default=(now() + timedelta(hours=48)),
    )

    def check_is_activation_key_expired(self):
        """Метод проверяет не вышел ли срок у ключа активации,
        который был отправлен пользователю на email при регистрации"""

        if now() <= self.activation_key_expires:
            return False
        else:
            return True
