from django.urls import reverse
from django.shortcuts import HttpResponseRedirect, render
from django.contrib import auth

from authapp.forms import UserRegisterForm
from authapp.models import User
from authapp.services.email import send_verification_email


def save_new_user_data(request):
    """" Сохраняет данные нового юзера и отправляет ему письмо для подтверждения регистрации.
    Возвращает редирект на страницу товаров """

    register_form = UserRegisterForm(request.POST, request.FILES)
    if register_form.is_valid:
        user = register_form.save()
        send_verification_email(user)
        return HttpResponseRedirect(reverse('productapp:products'))
    else:
        return HttpResponseRedirect(reverse('productapp:products'))


def activate_new_user(request, email, activation_key):
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
        elif user.activation_key == activation_key and user.check_is_activation_key_expired() and\
                user.is_active is not True:
            send_verification_email(user)
            return 'Ваш ключ активации истек. Мы отправили Вам новый. Провербте свой почтовый ящик'
        else:
            return f'error activation user: {user}'
    except Exception as ex:
        return f'error activation user : {ex.args}'
