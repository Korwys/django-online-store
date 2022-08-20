import logging

from django.shortcuts import get_object_or_404

from productapp.models import Product
from wishapp.models import WishList

logger = logging.getLogger('django_logger')


def save_selected_product(request, pk: int) -> None:
    """Сохраняет выбранный товар в WishList db"""
    try:
        product = get_object_or_404(Product, pk=pk)
        wishlist_item = WishList(user=request.user, product=product)
        wishlist_item.save()
    except TypeError as e:
        logger.error(e)


def remove_selected_product(pk: int) -> None:
    """Удаляет выбранный товар из WishList и если в избранном меньше 1 товара то вернет None """
    try:
        product = get_object_or_404(WishList, pk=pk)
        product.delete()
    except TypeError as e:
        logger.error(e)
        print('ok')


def count_whishlist_products_by_user(request) -> int:
    """Возвращает количество товаров в избранном"""
    return WishList.objects.filter(user=request.user).count()


def get_all_products_in_wishlist_by_user(request) -> WishList:
    """Возвращает список всех товаров которые юзер добавил в избранное"""
    return WishList.objects.filter(user=request.user)
