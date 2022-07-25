from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class User(AbstractUser):

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
