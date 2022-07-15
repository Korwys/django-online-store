from django.shortcuts import render, get_object_or_404

from productapp.models import Product, ProductCategory, Genders


def products(request, pk=None):
    title = 'Каталог'
    gender_choise_list = Genders.objects.all()
    categories = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all()
            gender = {'name': 'All'}
        else:
            gender = get_object_or_404(Genders, pk=pk)
            products = Product.objects.filter(gender__pk=pk)
            categories = []
            for item in products:
                if item.category not in categories:
                    categories.append(item.category)
        context = {
            'gender': gender,
            'products': products,
            'gender_choise_list': gender_choise_list,
            'categories': categories,
        }
        return render(request, 'productapp/products.html', context)

    products = Product.objects.all()
    context = {
        'title': title,
        'products': products,
        'gender_choise_list': gender_choise_list,
        'categories': categories,
    }
    return render(request, 'productapp/products.html', context)


def category(request, pk):
    gender_choise_list = Genders.objects.all()
    categories = ProductCategory.objects.all()
    gender_id = request.META.get('HTTP_REFERER')[-2]

    if gender_id.isnumeric():
        products = Product.objects.filter(category__pk=pk, gender__pk=gender_id)
        context = {
            'products': products,
            'gender_choise_list': gender_choise_list,
            'categories': categories,
        }
        return render(request, 'productapp/products.html', context)
    else:
        products = Product.objects.filter(category__pk=pk)
        context = {
            'products': products,
            'gender_choise_list': gender_choise_list,
            'categories': categories,
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
