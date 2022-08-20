from django.db.models import Sum

from cartapp.models import Cart
from orderapp.models import Order
from wishapp.models import WishList
from productapp.models import Genders, ProductCategory, Product


def genders_list(request):
    return {'gender_choise_list': Genders.objects.all()}


def product_categories(request):
    return {'categories': ProductCategory.objects.all()}


def products(request):
    return {'products': Product.objects.all()}


def cart_total_quantity(request):
    """Если пользователь аутентифицирован, то вернет текущий список объектов в корзине пользователя, иначе пустая строка"""

    products_count = Cart.objects.filter(user=request.user).aggregate(Sum('quantity'))
    if products_count['quantity__sum'] > 0:
        return {'total_products_quantity': products_count['quantity__sum']}
    else:
        return {'total_products_quantity': ' '}


def get_user_products_in_wishlist(request):
    """Если пользователь аутентифицирован то вернет список всех товаров в избранном у данного пользователя"""

    if request.user.is_authenticated:
        return {'wishlist_products': WishList.objects.filter(user=request.user).count()}
    else:
        return {'wishlist_products': ' '}


def get_user_orders(request):
    """Если пользователб аутентифицирован то вернет список всех товаров в избранном у данного пользователя"""
    order_count = Order.objects.filter(user=request.user, is_active=True).count()

    if order_count > 0:
        return {'user_orders': order_count}
    else:
        return {'user_orders': ' '}
