from django.shortcuts import render


def index(request):
    title = 'Каталог'

    context = {
        'title': title,
    }
    return render(request, 'productapp/products.html', context)

