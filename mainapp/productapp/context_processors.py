from cartapp.models import Cart
from .models import Genders, ProductCategory, Product


def genders_list(request):
    return {'gender_choise_list': Genders.objects.all()}


def product_categories(request):
    return {'categories': ProductCategory.objects.all()}


def products(request):
    return {'products': Product.objects.all()}


def cart_total_quantity(request):
    if request.user.is_authenticated:
        return {'user_products': Cart.objects.filter(user=request.user)}
    else:
        return {'user_products': ' '}
