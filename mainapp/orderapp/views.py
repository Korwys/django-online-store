from django.shortcuts import render, reverse, HttpResponseRedirect

from core.view_logger import view_logger
from orderapp.forms import OrderCreateForm
from orderapp.services.crud import get_all_orders_by_user, \
    change_order_status_and_save, transfer_products_from_cart_to_orderitem


@view_logger
def get_all_user_orders_view(request):
    """Возвращает страницу со списком  всех заказов юзера """

    all_orders = get_all_orders_by_user(request)
    return render(request, 'orderapp/orders.html', {'all_orders': all_orders})


# @view_logger
def create_user_order_view(request):
    """
    Возвращает в случае GET пустую форму для создания заказа,а в случае POST, проверит валидность формы, если форма
    валидна, то создаст заказ. Товары из заказа будут добавлены в структуру заказа, корзина будет очищена
    """

    form = OrderCreateForm(request.POST or None)
    form.instance.user = request.user
    if form.is_valid():
        order = form.save()
        transfer_products_from_cart_to_orderitem(request, order)
        return HttpResponseRedirect(reverse('orderapp:orders'))
    else:
        return render(request, 'orderapp/create.html', {'form': form})


@view_logger
def cancel_user_order_view(request, pk):
    """После отмены заказа вернет туже самую страницу страницу, но статус заказа будет изменен"""
    change_order_status_and_save(pk)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
