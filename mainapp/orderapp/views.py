from django.shortcuts import render, HttpResponseRedirect

from core.view_logger import view_logger
from orderapp.forms import OrderCreateForm
from orderapp.services.crud import get_all_orders_by_user, \
    change_order_status, create_new_user_order


@view_logger
def get_all_user_orders_view(request):
    """Возвращает страницу со списком  всех заказов юзера """

    all_orders = get_all_orders_by_user(request)
    return render(request, 'orderapp/orders.html', {'all_orders': all_orders})


@view_logger
def create_user_order_view(request):
    """
    Возвращает в случае GET пустую форму для создания заказа,а в случае POST, проверит валидность формы, если форма
    валидна, то создаст заказ. Товары из заказа будут добавлены в структуру заказа, корзина будет очищена
    """
    if request.method == 'POST':
        return create_new_user_order(request)
    else:
        return render(request, 'orderapp/create.html', {'form': OrderCreateForm()})


@view_logger
def cancel_user_order_view(request, pk):
    """После отмены заказа вернет туже самую страницу страницу, но статус заказа будет изменен"""
    change_order_status(pk)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
