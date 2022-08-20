from django.db import models
from django.conf import settings

from productapp.models import Product


class Order(models.Model):
    """Модель описывает заказ юзера. Поля:юзер, город,адрес, индекс, статус,is_active, дата создания и редактирования
    Описаны статусы заказы, которые присваются заказу на разных стадиях (оплачен, формируется и проч.)"""
    PROCESSING = 'PCG'
    ASSEMBLY = 'ABL'
    PAID = 'PD'
    READY = 'RDY'
    CANCEL = 'CNL'

    ORDER_STATUS_CHOICES = (
        (PROCESSING, 'формирование'),
        (ASSEMBLY, 'сборка заказа'),
        (PAID, 'оплачен'),
        (READY, 'готов к выдаче'),
        (CANCEL, 'отменен'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    city = models.CharField(
        max_length=20,
        verbose_name='Город',
    )

    address = models.CharField(
        max_length=150,
        verbose_name='Адрес',
    )

    postal_code = models.CharField(
        max_length=10,
        verbose_name='Индекс'
    )

    status = models.CharField(
        verbose_name='статус',
        max_length=3,
        choices=ORDER_STATUS_CHOICES,
        default=PAID
    )

    is_active = models.BooleanField(
        verbose_name='Активен/Неактивен',
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )

    class Meta:
        db_table = 'order'
        ordering = ('-created_at',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def get_orders_quantity(self):
        """Если количество активных заказов больше 0, то вернет их количество, иначе пустая строка"""
        order_count = Order.objects.filter(user=self.user, is_active=True).count()
        if order_count >0:
            return order_count
        else:
            return ""

    def get_total_quantity(self):
        """Вернет общее количество товаров в заказе"""

        items = self.orderitems.selected_related
        return sum(list(map(lambda x: x.quantity, items)))

    def get_product_type_quantity_in_order(self):
        """Вернет общее количество товарых позиций в заказе"""

        items = self.orderitems.selected_related
        return len(items)

    def get_total_cost(self):
        """ Вернет общую стоимость заказа"""
        items = self.orderitems.selected_related
        return sum(list(map(lambda x: x.product.price * x.quantity, items)))


class OrderItem(models.Model):
    """Модель описывает структуру заказа.(товарная позиция - количество)"""
    order = models.ForeignKey(
        Order,
        related_name='orderitems',
        on_delete=models.CASCADE,
        verbose_name='Заказ'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Товар'
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Количество',
        default=0
    )

    def get_product_cost(self):
        """Вернет стоимость товара с учетом количества"""

        return self.product.price * self.quantity

    class Meta:
        db_table = 'orderitem'
        verbose_name = 'Структура заказа'
        verbose_name_plural = 'Структура заказа'
