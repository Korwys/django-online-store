from django.shortcuts import render, get_object_or_404

from core.view_logger import view_logger
from .models import Product
from .services.crud import filtering_products_by_gender, filtering_product_by_category, filtering_related_products, \
    paginate


@view_logger
def get_all_products(request):
    """Вернет всe товары на главной странице каталога"""

    context = {
        'title': 'Каталог',
        'products': paginate(request),
        'current_sort': request.GET.get('sorting'),
    }
    return render(request, 'productapp/products.html', context)


@view_logger
def get_products_by_gender(request, pk: int):
    """ Вернет список товаров при фильтрации по полу"""

    context = filtering_products_by_gender(request, pk)
    return render(request, 'productapp/products.html', context)


@view_logger
def get_products_by_category(request, pk: int):
    """ Вернет список товаров при фильтрации по категории"""

    context = filtering_product_by_category(request, pk)
    return render(request, 'productapp/products.html', context)


@view_logger
def get_single_product_page(request, pk: int):
    """ Вернет карточку товара,а так же, связанные товары сортированные по полу,
        который соответсвует товару из карточки"""

    product = get_object_or_404(Product, pk=pk)
    context = {
        'title': 'Страница продукта',
        'product': product,
        'products': filtering_related_products(product),
    }
    return render(request, 'productapp/single_product.html', context)
