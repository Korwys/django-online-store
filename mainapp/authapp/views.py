from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from .forms import UserLoginForm, UserRegisterForm
from .models import User
from .services.crud import save_new_user_data, activate_new_user


def user_login(request):
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


def new_user_registration(request):
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
