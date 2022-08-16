import logging
import random

from django.core.paginator import Paginator

from productapp.models import Product, Brand

logger = logging.getLogger('django_logger')


def filtering_products_by_gender(request, pk: int) -> dict:
    """Фильтрует список товаров по выбранному полу"""
    try:
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
    except (TypeError, ValueError) as e:
        logger.error(e)


def filtering_product_by_category(request, pk: int) -> dict:
    """Фильтрует список товаров по выбранной категории"""
    try:
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
    except (TypeError, ValueError) as e:
        logger.error(e)


def filtering_related_products(product) -> Product:
    """ Фильтрует список товаров на основе пола товара из карточки."""

    return Product.objects.filter(gender__pk=product.gender.pk).exclude(name=product.name)


def sorting_products_by_type(request, pk=None) -> Product:
    """ Сортирует товары по алфавиту или по цене """

    all_sorting_types = {
        'name': 'name',
        'name_desc': '-name',
        'price': 'price',
        'price_desc': '-price'
    }
    try:
        get_sorting_type = request.GET.get('sorting')
        if 'gender' in request.path and get_sorting_type:
            return Product.objects.filter(gender__pk=pk).order_by(all_sorting_types[get_sorting_type])
        elif 'gender' in request.path:
            return Product.objects.filter(gender__pk=pk)

        if get_sorting_type and pk:
            return Product.objects.filter(category__pk=pk).order_by(all_sorting_types[get_sorting_type])

        if get_sorting_type is not None:
            return Product.objects.all().order_by(all_sorting_types[get_sorting_type])
        else:
            return Product.objects.all()
    except (TypeError, ValueError) as e:
        logger.error(e)


def paginate(request, *args, pk=None) -> Paginator:
    """ Реализиует пагинацию на страницах"""
    try:
        if request.GET.get('sorting'):
            paginator = Paginator(sorting_products_by_type(request, pk), 6)
            page_number = request.GET.get('page')
            return paginator.get_page(page_number)
        elif args:
            paginator = Paginator(args[0], 6)
            page_number = request.GET.get('page')
            return paginator.get_page(page_number)
        else:
            paginator = Paginator(Product.objects.all(), 6)
            page_number = request.GET.get('page')
            return paginator.get_page(page_number)
    except (TypeError, ValueError) as e:
        logger.error(e)


def get_all_brands():
    return Brand.objects.all()


def get_hot_product():
    product = Product.objects.all()
    return random.sample(list(product), 3)
