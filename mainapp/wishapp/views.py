from django.shortcuts import render, HttpResponseRedirect, reverse

from core.view_logger import view_logger
from wishapp.services.crud import save_selected_product, remove_selected_product, count_whishlist_products_by_user, \
    get_all_products_in_wishlist_by_user


@view_logger
def get_all_user_wishlist_products(request):
    """Возвращает все продукты которые юзер добавил в избранное"""

    products_in_wishlist = get_all_products_in_wishlist_by_user(request)
    return render(request, 'wishapp/wishlist.html', {'products_in_wishlist': products_in_wishlist})


@view_logger
def add_product_in_wishlist(request, pk):
    """Добавляет выбранный товар в Избранное"""

    save_selected_product(request, pk)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@view_logger
def remove_product_from_wishlist(request, pk):
    """Удаляет выбранный товар из Избранного и если в Избранном меньше 1 товара редиректит юзера на главную"""

    remove_selected_product(pk)

    if count_whishlist_products_by_user(request) < 1:
        return HttpResponseRedirect(reverse('index'))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
