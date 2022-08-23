import logging
import random

from django.core.paginator import Paginator
from django.db.models import Q

from productapp.models import Product, Brand, ProductCategory

logger = logging.getLogger('django_logger')


def filtering_related_products(product) -> Product:
    """ Вернет список товаров отфильтрованный по такому же гендеру как и у товара из карточки"""

    return Product.objects.filter(gender__pk=product.gender.pk).exclude(name=product.name)


def sorting_products_by_type(request) -> Product:
    """ Сортирует товары по алфавиту или по цене """

    all_sorting_types = {
        'name': 'name',
        'name_desc': '-name',
        'price': 'price',
        'price_desc': '-price'
    }
    income_values = {
        'brand': request.GET.get('brand'),
        'gender': request.GET.get('gender'),
        'category': request.GET.get('category')
    }

    query = []
    for i in income_values.keys():
        if i == 'brand' and income_values[i] != "" and income_values[i] is not None:
            query.append(Q(brand__id=income_values[i]))
        if i == 'category' and income_values[i] != "" and income_values[i] is not None:
            query.append(Q(category__id=income_values[i]))
        if i == 'gender' and income_values[i] != "" and income_values[i] is not None:
            query.append(Q(gender__id=income_values[i]))

    get_sorting_type = request.GET.get('sorting')

    return Product.objects.select_related('brand', 'category') \
        .only('name', 'price', 'image', 'brand__name', 'category__name') \
        .filter(*query) \
        .order_by(all_sorting_types[get_sorting_type])


def paginate(request, *args) -> Paginator:
    """ Реализиует пагинацию на страницах"""
    try:
        if request.GET.get('sorting'):
            paginator = Paginator(sorting_products_by_type(request), 6)
            page_number = request.GET.get('page')
            return paginator.get_page(page_number)
        elif args:
            paginator = Paginator(args[0], 6)
            page_number = request.GET.get('page')
            return paginator.get_page(page_number)
        else:
            paginator = Paginator(
                Product.objects.all().select_related('brand', 'category').only('name', 'price', 'image', 'brand__name',
                                                                               'category__name'), 6)
            page_number = request.GET.get('page')
            return paginator.get_page(page_number)
    except (TypeError, ValueError) as e:
        logger.error(e)


def get_all_brands() -> Brand:
    return Brand.objects.all()


def get_hot_product() -> list:
    product = Product.objects.all().only('image')
    return random.sample(set(product), 3)


def get_all_category() -> ProductCategory:
    return ProductCategory.objects.all().only('name','image')
