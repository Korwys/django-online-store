from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegisterForm, UserEditForm
from .services.crud import save_new_user_data, activate_new_user


def user_login(request):
    """ Логинит пользователя на сайте"""

    login_form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
    context = {'login_form': login_form}
    return render(request, 'authapp/login.html', context)


def user_logout(request):
    """Разлогинивает пользователя"""

    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def edit_user_profile(request):
    """Редактирует профиль пользователя"""

    if request.method == 'POST':
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit_user_profile'))
    else:
        context = {
            'title': 'Редактирование профиля',
            'edit_form': UserEditForm(instance=request.user),
        }
        return render(request, 'authapp/edit.html', context)


def registers_new_user(request):
    """ Регистрирует нового пользователя """

    if request.method == 'POST':
        return save_new_user_data(request)
    else:
        context = {
            'register_form': UserRegisterForm(),
        }
    return render(request, 'authapp/register.html', context)


def confirm_new_user_registration(request, email, activation_key):
    """ Отображает юзеру результат верификации на сайте после перехода по ссылке из отправленого нами письма"""

    contex = {
        'activation_result_info': activate_new_user(request, email, activation_key)
    }
    return render(request, 'authapp/verification.html', contex)
