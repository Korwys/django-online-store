from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from productapp.models import Product, ProductCategory, Genders


def products(request, pk=None):
    title = 'Каталог'
    current_sort = request.GET.get('sorting')
    context = {
        'title': title,
        'products': pages_paginator(request),
        'current_sort': current_sort,
    }
    return render(request, 'productapp/products.html', context)


def filter_by_gender(request, pk):
    current_sort = request.GET.get('sorting')

    if 'category' in request.META.get('HTTP_REFERER'):
        category_from_request = request.META.get('HTTP_REFERER')[-2]
        products = Product.objects.filter(gender__pk=pk, category__pk=category_from_request)
        context = {
            'products': pages_paginator(request, products),
            'current_sort': current_sort,
        }
        return render(request, 'productapp/products.html', context)
    else:
        products_by_gender = Product.objects.filter(gender__pk=pk)
        categories = set(item.category for item in products_by_gender)
        context = {
            'products': pages_paginator(request, products_by_gender, pk=pk),
            'current_sort': current_sort,
            'categories': categories,
        }
        return render(request, 'productapp/products.html', context)


def filter_by_category(request, pk):
    current_sort = request.GET.get('sorting')
    if 'gender' in request.META.get('HTTP_REFERER'):
        gender_id = request.META.get('HTTP_REFERER')[-2]
        products = Product.objects.filter(category__pk=pk, gender__pk=gender_id)
        context = {'products': pages_paginator(request)}
        return render(request, 'productapp/products.html', context)
    else:
        products_by_category = Product.objects.filter(category__pk=pk)
        context = {
            'products': pages_paginator(request, products_by_category, pk=pk),
            'current_sort': current_sort,
        }
        return render(request, 'productapp/products.html', context)


def single_product_page(request, pk):
    title = 'Страница продукта'
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(gender__pk=product.gender.pk).exclude(name=product.name)
    context = {
        'title': title,
        'product': product,
        'products': related_products,
    }
    return render(request, 'productapp/single_product.html', context)


def sorting_products_by_type(request, pk=None) -> Product:
    """ Сортирует товары по алфавиту и по цене """

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


def pages_paginator(request, *args, pk=None):
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
