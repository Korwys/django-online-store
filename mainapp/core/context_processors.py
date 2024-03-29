from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from cartapp.models import Cart
from orderapp.models import Order
from wishapp.models import WishList


def cart_total_quantity(request):
    """Если пользователь аутентифицирован, то вернет текущий список объектов в корзине пользователя,
     иначе пустая строка"""

    if request.user.is_authenticated:
        products_count = Cart.objects.filter(user=request.user).aggregate(Sum('quantity'))
        if products_count['quantity__sum'] is None:
            return {'total_products_quantity': ''}
        if products_count['quantity__sum'] > 0:
            return {'total_products_quantity': products_count['quantity__sum']}
    else:
        return {'total_products_quantity': ''}


def get_user_products_in_wishlist(request):
    """Если пользователь аутентифицирован, то вернет список всех товаров в избранном у данного пользователя"""

    if request.user.is_authenticated:
        wishlist_count = WishList.objects.filter(user=request.user).count()
        if wishlist_count > 0:
            return {'wishlist_products': wishlist_count}
        else:
            return {'wishlist_products': ''}
    else:
        return {'wishlist_products': ''}


def get_user_orders(request):
    """Если пользователь аутентифицирован, то вернет список всех товаров в избранном у данного пользователя"""

    if request.user.is_authenticated:
        order_count = Order.objects.filter(user=request.user, is_active=True).count()

        if order_count > 0:
            return {'user_orders': order_count}
        else:
            return {'user_orders': ''}
    else:
        return {'user_orders': ''}
