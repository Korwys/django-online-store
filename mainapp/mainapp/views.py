from django.shortcuts import render


def index(request):
    title = 'Главная'
    context = {
        'title': title,
    }
    return render(request, 'mainapp/index.html', context)


def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'mainapp/contact.html', context)


def about(request):
    title = 'О нас'
    context = {
        'title': title,
    }
    return render(request, 'mainapp/about.html', context)
