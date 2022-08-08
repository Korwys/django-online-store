import os
from hashlib import pbkdf2_hmac

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from .models import User


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(min_length=8)
    password2 = forms.CharField(min_length=8)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-styling'
            field.help_text = ''

    def save(self):
        user = super(UserRegisterForm, self).save()
        user.is_active = False
        salt = os.urandom(16)
        user.activation_key = pbkdf2_hmac('sha1', b'user.email', salt, 1000).hex()
        user.save()
        return user


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-styling'
            field.help_text = ''
