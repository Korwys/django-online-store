from django.core.paginator import Paginator

from productapp.models import Product


def sorting_products_by_type(request, pk=None) -> Product:
    """ Сортирует товары по алфавиту или по цене """

    all_sorting_types = {
        'name': 'name',
        'name_desc': '-name',
        'price': 'price',
        'price_desc': '-price'
    }
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


def paginate(request, *args, pk=None) -> Paginator:
    """ Реализиует пагинацию на страницах"""

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

