from django.shortcuts import get_object_or_404, render

from cartapp.services.crud import get_cart_products_by_user
from orderapp.models import OrderItem, Order


def transfer_products_from_cart_to_orderitem(request, order) -> None:
    """"После создания заказа  товары из корзины перемещает в OrderItem и очищает корзину"""

    cart = get_cart_products_by_user(request)
    for item in cart:
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
    cart.delete()


def get_all_orders_by_user(request) -> Order:
    """Возвращает список всех заказов пользователя(активные, отмененные)"""

    return Order.objects.filter(user=request.user)


def change_order_status_and_save(pk: int) -> None:
    """Меняет статус заказа на CNL(отменен)+ is_active=False"""

    user_order = get_object_or_404(Order, pk=pk)
    user_order.status = 'CNL'
    user_order.is_active = False
    user_order.save()
