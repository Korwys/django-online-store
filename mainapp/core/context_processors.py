from cartapp.models import Cart
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

    if request.user.is_authenticated:
        return {'user_products': Cart.objects.filter(user=request.user)}
    else:
        return {'user_products': ' '}


def get_user_products_in_wishlist(request):
    """Если пользователб аутентифицирован то вернет список всех товаров в избранном у данного пользователя"""

    if request.user.is_authenticated:
        return {'wishlist_products': WishList.objects.filter(user=request.user)}
    else:
        return {'wishlist_products': ' '}
