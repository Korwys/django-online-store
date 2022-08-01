from django.shortcuts import get_object_or_404

from productapp.models import Product
from wishapp.models import WishList


def save_selected_product(request, pk: int):
    """Сохраняет выбранный товар в WishList db"""

    product = get_object_or_404(Product, pk=pk)
    wishlist_item = WishList(user=request.user, product=product)
    wishlist_item.save()


def remove_selected_product(request, pk: int):
    """Удаляет выбаранный товар из WishList db """
    
    product = get_object_or_404(WishList, pk=pk)
    product.delete()
