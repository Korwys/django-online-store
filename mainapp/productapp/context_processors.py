from django.core.paginator import Paginator

from .models import Genders, ProductCategory, Product


def genders_list(request):
    return {'gender_choise_list': Genders.objects.all()}


def product_categories(request):
    return {'categories': ProductCategory.objects.all()}


def products(request):
    return {'products': Product.objects.all()}
