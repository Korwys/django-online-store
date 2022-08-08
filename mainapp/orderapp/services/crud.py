import logging

from django.shortcuts import get_object_or_404, HttpResponseRedirect, reverse, render

from cartapp.services.crud import get_cart_products_by_user
from orderapp.forms import OrderCreateForm
from orderapp.models import OrderItem, Order

logger = logging.getLogger('django_logger')


def create_new_user_order(request):
    """Принимает данные в форму для создания заказа, проверяет валидность данных, сохраняет данные в бд.
    Далее, берет товары текущего заказа из корзины и переносит их в модель OrderItem. Удаляет товары из заказа"""
    try:
        form = OrderCreateForm(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            order = form.save()
            transfer_products_from_cart_to_orderitem(request, order)
            return HttpResponseRedirect(reverse('orderapp:orders'))
        else:
            return render(request, 'orderapp/create.html', {'form': form})
    except (TypeError, ValueError) as e:
        logger.error(e)


def transfer_products_from_cart_to_orderitem(request, order) -> None:
    """"После создания заказа  товары из корзины перемещает в OrderItem и очищает корзину"""
    try:
        cart = get_cart_products_by_user(request)
        for item in cart:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        cart.delete()
    except (TypeError, ValueError) as e:
        logger.error(e)


def get_all_orders_by_user(request) -> Order:
    """Возвращает список всех заказов пользователя(активные, отмененные)"""

    return Order.objects.filter(user=request.user)


def change_order_status(pk: int) -> None:
    """Меняет статус заказа на CNL(отменен)+ is_active=False"""
    try:
        user_order = get_object_or_404(Order, pk=pk)
        user_order.status = 'CNL'
        user_order.is_active = False
        user_order.save()
    except (TypeError, ValueError) as e:
        logger.error(e)
