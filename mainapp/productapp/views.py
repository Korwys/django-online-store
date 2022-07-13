from django.shortcuts import render

from productapp.models import Product, ProductCategory, Genders


def index(request):
    title = 'Каталог'

    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    genders = Genders.objects.all()

    context = {
        'title': title,
        'products': products,
        'categories': categories,
        'genders': genders,

    }
    return render(request, 'productapp/products.html', context)
