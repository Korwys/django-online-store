from django.shortcuts import render, HttpResponseRedirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .services.crud import get_cart_products_by_user, add_selected_product_in_cart, remove_selected_product_from_cart, \
    change_product_quantity

@login_required
def get_user_cart(request):
    """Отображает товары в корзине пользователя"""

    context = {
        'user_products': get_cart_products_by_user(request)
    }
    return render(request, 'cartapp/cart.html', context)

@login_required
def add_product_in_cart(request, pk: int):
    """Добавляет товар в корзину"""

    add_selected_product_in_cart(request, pk)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def remove_product_from_cart(request, pk: int):
    """Удаляет товар из корзины"""

    remove_selected_product_from_cart(pk)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def edit_user_cart(request, pk: int, quantity: int):
    """Изменяет количество товара в корзине и возвращает ответ в json"""
    if request.accepts('XMLHttpRequest'):
        cart_product_list_after_edit = change_product_quantity(request, pk, quantity)
        context = {
            'user_products': cart_product_list_after_edit
        }
        result = render_to_string('cartapp/includes/inc_cart_product_list.html', context)
        return JsonResponse({'result': result})
