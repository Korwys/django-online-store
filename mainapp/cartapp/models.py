from django.db import models
from django.conf import settings
from django.db.models import Sum

from productapp.models import Product


class Cart(models.Model):
    """Модель описывает данные пользовательской корзины."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Количество',
        default=0
    )

    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    @property
    def product_cost(self):
        """Метод возвращает итоговую стоимость товара с учетом его количества"""
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        """Метод возвращает сумму всех товаров в корзине"""
        cart_user_list = Cart.objects.filter(user=self.user).aggregate(Sum('quantity'))
        # return  sum(list(map(lambda x: x.quantity, cart_user_list)))
        return cart_user_list['quantity__sum']

    @property
    def total_cost(self):
        """Метод возвращает итоговую стоимость за все товары в корзине"""
        cart_user_list = Cart.objects.filter(user=self.user)
        return sum(list(map(lambda x: x.product_cost, cart_user_list)))
