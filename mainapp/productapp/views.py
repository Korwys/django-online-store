from django.shortcuts import render, get_object_or_404

from core.filters import ProductFilter
from core.view_logger import view_logger
from .models import Product
from .services.crud import filtering_related_products,paginate, get_all_brands


# @view_logger
def get_all_products(request):
    """Вернет всe товары на главной странице каталога"""

    filter_obj = ProductFilter(request.GET, queryset=Product.objects.all())

    context = {
        'title': 'Каталог',
        'products': paginate(request, filter_obj.qs),
        'current_sort': request.GET.get('sorting'),
        'brands': get_all_brands(),
        'filter': filter_obj
    }
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
