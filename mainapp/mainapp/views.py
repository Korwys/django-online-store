from django.shortcuts import render

from core.view_logger import view_logger


@view_logger
def index(request):
    title = 'Главная'
    context = {
        'title': title,
    }
    return render(request, 'mainapp/index.html', context)


@view_logger
def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'mainapp/contact.html', context)


@view_logger
def about(request):
    title = 'О нас'
    context = {
        'title': title,
    }
    return render(request, 'mainapp/about.html', context)
