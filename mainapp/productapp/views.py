from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from productapp.models import Product, ProductCategory, Genders


def products(request, pk=None):
    title = 'Каталог'
    current_sort = request.GET.get('sorting')
    gender_choise_list = Genders.objects.all()
    categories = ProductCategory.objects.all()
    category_from_request = 0

    if 'category' in request.META.get('HTTP_REFERER'):
        category_from_request = request.META.get('HTTP_REFERER')[-2]
        gender = get_object_or_404(Genders, pk=pk)
        products = Product.objects.filter(gender__pk=pk, category__pk=category_from_request)

        context = {
            'gender': gender,
            'products': products,
            'gender_choise_list': gender_choise_list,
            'categories': categories,
            'current_sort': current_sort,
        }
        return render(request, 'productapp/products.html', context)
    else:
        if pk is not None:
            if pk == 0:
                products = Product.objects.all()
                gender = {'name': 'All'}
            else:
                gender = get_object_or_404(Genders, pk=pk)
                products = sorting(request, pk)
                categories = []
                for item in products:
                    if item.category not in categories:
                        categories.append(item.category)

            paginator = Paginator(products, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            context = {
                'gender': gender,
                'products': page_obj,
                'gender_choise_list': gender_choise_list,
                'categories': categories,
                'current_sort': current_sort,
            }
            return render(request, 'productapp/products.html', context)

    paginator_products = sorting(request)
    paginator = Paginator(paginator_products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': title,
        'products': page_obj,
        'gender_choise_list': gender_choise_list,
        'categories': categories,
        'current_sort': current_sort,
    }

    return render(request, 'productapp/products.html', context)


def category(request, pk):
    gender_choise_list = Genders.objects.all()
    categories = ProductCategory.objects.all()
    current_sort = request.GET.get('sorting')

    if 'gender' in request.META.get('HTTP_REFERER'):
        gender_id = request.META.get('HTTP_REFERER')[-2]
        products = Product.objects.filter(category__pk=pk, gender__pk=gender_id)
        context = {
            'products': products,
            'gender_choise_list': gender_choise_list,
            'categories': categories,
        }
        return render(request, 'productapp/products.html', context)

    else:
        if request.GET.get('sorting'):
            products = sorting(request, pk)
        else:
            products = Product.objects.filter(category__pk=pk)

        context = {
            'products': products,
            'gender_choise_list': gender_choise_list,
            'categories': categories,
            'current_sort': current_sort,
        }
        return render(request, 'productapp/products.html', context)


def single_product(request, pk):
    title = 'Страница продукта'
    product = get_object_or_404(Product, pk=pk)
    products = Product.objects.all()

    context = {
        'title': title,
        'product': product,
        'products': products,
    }
    return render(request, 'productapp/single_product.html', context)


def sorting(request, pk=None):
    sorting_types = {
        'name': 'name',
        'name_desc': '-name',
        'price': 'price',
        'price_desc': '-price'
    }
    get_sorting_type = request.GET.get('sorting')

    if 'gender' in request.path and get_sorting_type:
        return Product.objects.filter(gender__pk=pk).order_by(sorting_types[get_sorting_type])
    elif 'gender' in request.path:
        return Product.objects.filter(gender__pk=pk)

    if get_sorting_type and pk:
        return Product.objects.filter(category__pk=pk).order_by(sorting_types[get_sorting_type])

    if get_sorting_type is not None:
        return Product.objects.all().order_by(sorting_types[get_sorting_type])
    else:
        return Product.objects.all()
