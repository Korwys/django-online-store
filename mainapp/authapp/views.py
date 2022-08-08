from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from core.view_logger import view_logger
from .forms import UserLoginForm, UserRegisterForm, UserEditForm
from .services.crud import save_new_user_data, activate_new_user, edit_user_data, login_user_on_site


@view_logger
def user_login(request):
    """ Логинит пользователя на сайте"""
    if request.method == 'POST':
        return login_user_on_site(request)
    else:
        return render(request, 'authapp/login.html', {'login_form': UserLoginForm()})


@view_logger
def user_logout(request):
    """Разлогинивает пользователя"""

    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@view_logger
@login_required
def edit_user_profile(request):
    """Редактирует профиль пользователя"""

    if request.method == 'POST':
        return edit_user_data(request)
    else:
        return render(request, 'authapp/edit.html', {'edit_form': UserEditForm(instance=request.user)})


# @view_logger
def registers_new_user(request):
    """ Регистрирует нового пользователя """

    if request.method == 'POST':
        return save_new_user_data(request)
    else:
        return render(request, 'authapp/register.html', {'register_form': UserRegisterForm()})


@view_logger
def confirm_new_user_registration(request, email, activation_key):
    """ Отображает юзеру результат верификации на сайте после перехода по ссылке из отправленого нами письма"""

    contex = {
        'activation_result_info': activate_new_user(request, email, activation_key)
    }
    return render(request, 'authapp/verification.html', contex)
