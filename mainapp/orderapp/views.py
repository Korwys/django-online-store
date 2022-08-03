from django.shortcuts import render, reverse, HttpResponseRedirect

from cartapp.services.crud import get_cart_products_by_user
from orderapp.forms import OrderCreateForm
from orderapp.services.crud import create_new_object_in_order_and_orderitem, get_all_orders_by_user, \
    change_order_status_and_save


def get_all_user_orders_view(request):
    """Возвращает страницу со списком  всех заказов юзера """

    all_orders = get_all_orders_by_user(request)
    return render(request, 'orderapp/orders.html', {'all_orders': all_orders})


def create_user_order_view(request):
    """Возвращает в случае GET пустую форму для создания заказа, в случае POST вернет редирект на страницу заказов"""

    cart = get_cart_products_by_user(request)
    if request.method == 'POST':
        create_new_object_in_order_and_orderitem(request, cart)
        return HttpResponseRedirect(reverse('orderapp:orders'))
    else:
        form = OrderCreateForm()
    return render(request, 'orderapp/create.html', {'form': form})


def cancel_user_order_view(request, pk):
    """После отмены заказа вернет туже самую страницу страницу, но статус заказа будет изменен"""
    change_order_status_and_save(pk)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
