import logging

from django.shortcuts import get_object_or_404, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum

from cartapp.models import Cart
from productapp.models import Product

logger = logging.getLogger('django_logger')


def get_cart_products_by_user(request):
    """ Возвращает список товаров в корзине пользователя"""

    return Cart.objects.filter(user=request.user).select_related('product')


def add_selected_product_in_cart(request, pk: int) -> None:
    """Добавляет выбранный товар в корзину"""
    try:
        selected_product = get_object_or_404(Product, pk=pk)
        cart_item = Cart.objects.filter(user=request.user, product=selected_product).first()

        if not cart_item:
            cart_item = Cart(user=request.user, product=selected_product)

        cart_item.quantity += 1
        cart_item.save()
    except (TypeError, ValueError, Http404) as e:
        logger.error(e)


def remove_selected_product_from_cart(pk: int) -> None:
    """Удаляет выбранный товар из корзины"""

    try:
        selected_product = get_object_or_404(Cart, pk=pk)
        selected_product.delete()
    except (ObjectDoesNotExist, Http404) as e:
        logger.error(e)


def change_product_quantity(request, pk: int, quantity: int) -> Cart:
    """Изменяет количество выбранного товара в корзине"""
    try:
        product_quantity = int(quantity)
        cart_item = Cart.objects.get(product_id=pk)

        if product_quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()

        return Cart.objects.filter(user=request.user).order_by('product__price')
    except (TypeError, ValueError, Http404, ObjectDoesNotExist) as e:
        logger.error(e)
