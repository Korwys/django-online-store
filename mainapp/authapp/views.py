

from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from .forms import UserLoginForm, UserRegisterForm


def user_login(request):
    # login_form = UserLoginForm(request)
    login_form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
    content = {'login_form': login_form}
    return render(request, 'authapp/login.html', content)




def user_register(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid:
            user = register_form.save()
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        register_form = UserRegisterForm()

    context = {
        'register_form': register_form,
        }
    return render(request, 'authapp/register.html', context)
