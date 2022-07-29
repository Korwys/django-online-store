from django.shortcuts import get_object_or_404

from productapp.models import Product
from productapp.services.sorting import paginate


def filtering_products_by_gender(request, pk: int) -> dict:
    """Фильтрует список товаров по выбранному полу"""
    if 'category' in request.META.get('HTTP_REFERER'):
        category_from_request = request.META.get('HTTP_REFERER')[-2]
        products = Product.objects.filter(gender__pk=pk, category__pk=category_from_request)
        context = {
            'products': paginate(request, products),
            'current_sort': request.GET.get('sorting'),
        }
        return context
    else:
        products_by_gender = Product.objects.filter(gender__pk=pk)
        categories = set(item.category for item in products_by_gender)
        context = {
            'products': paginate(request, products_by_gender, pk=pk),
            'current_sort': request.GET.get('sorting'),
            'categories': categories,
        }
        return context


def filtering_product_by_category(request, pk: int) -> dict:
    """Фильтрует список товаров по выбранной категории"""
    if 'gender' in request.META.get('HTTP_REFERER'):
        gender_id = request.META.get('HTTP_REFERER')[-2]
        products = Product.objects.filter(category__pk=pk, gender__pk=gender_id)
        context = {
            'products': paginate(request),
            'current_sort': request.GET.get('sorting')
        }
        return context
    else:
        products_by_category = Product.objects.filter(category__pk=pk)
        context = {
            'products': paginate(request, products_by_category, pk=pk),
            'current_sort': request.GET.get('sorting'),
        }
        return context


def filtering_related_products(product):
    """ Фильтрует список товаров на основе пола товара из карточки."""

    return Product.objects.filter(gender__pk=product.gender.pk).exclude(name=product.name)
