from django.db import models
from django.conf import settings

from productapp.models import Product


class WishList(models.Model):
    """Модель описывает данные товаров добавленных в Избранное"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )

    class Meta:
        db_table = 'wishlist'
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    @property
    def get_total_quantity(self):
        """Метод возвращает количество товарных позиции в Избранном"""
        return WishList.objects.filter(user=self.user).count()
