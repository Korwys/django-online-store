import logging

from django.urls import reverse
from django.shortcuts import HttpResponseRedirect, render
from django.contrib import auth

from authapp.forms import UserRegisterForm, UserEditForm, UserLoginForm
from authapp.models import User
from authapp.services.email import send_verification_email

logger = logging.getLogger('django_logger')


def login_user_on_site(request):
    try:
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'authapp/login.html', {'login_form': login_form})
    except ValueError as e:
        logger.error(e)


def save_new_user_data(request) -> HttpResponseRedirect:
    """" Сохраняет данные нового юзера и отправляет ему письмо для подтверждения регистрации.
    Возвращает редирект на страницу товаров """
    try:
        register_form = UserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid:
            user = register_form.save()
            send_verification_email(user)
            return HttpResponseRedirect(reverse('productapp:products'))
        else:
            print(register_form.errors)
            return HttpResponseRedirect(reverse('productapp:products'))
    except ValueError as e:
        logger.error(e)


def edit_user_data(request) -> HttpResponseRedirect:
    """
    Вносит изменения в личные данные юзера.
    Возвращает редирект на страницу измененния данных, но уже с новыми данными
    """

    try:
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit_user_profile'))
    except ValueError as e:
        logger.error(e)


def activate_new_user(request, email: str, activation_key: str) -> str:
    """Активирует и логинит юзера при переходе по ссылке из отправленного нами письма при регистрации,
        при условии, что ключ активации совпадает с имеющимся и его срок не истек и
        возвращает сообщение о результате активации"""

    try:
        user = User.objects.get(email=email, activation_key=activation_key)
        if user.activation_key == activation_key and not user.check_is_activation_key_expired() \
                and user.is_active is not True:
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return ' Поздравляем! Вы успешно зарегистрировались!'
        elif user.activation_key == activation_key and user.is_active is True:
            return 'Ранее Вы уже подтвердили регистрацию!'
        elif user.activation_key == activation_key and user.check_is_activation_key_expired() and \
                user.is_active is not True:
            send_verification_email(user)
            return 'Ваш ключ активации истек. Мы отправили Вам новый. Провербте свой почтовый ящик'
        else:
            return f'error activation user: {user}'
    except (ValueError, TypeError) as e:
        logger.error(e)
