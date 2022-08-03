from django.shortcuts import get_object_or_404

from cartapp.models import Cart
from orderapp.forms import OrderCreateForm
from orderapp.models import OrderItem, Order


def create_new_object_in_order_and_orderitem(request, cart: Cart) -> None:
    """Создает новую запись в бд Order и OrderItem + удаляет товары из корзины текущего юзера"""

    form = OrderCreateForm(request.POST)
    form.instance.user = request.user
    if form.is_valid():
        order = form.save()
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )
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
