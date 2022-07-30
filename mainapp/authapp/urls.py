from django.urls import path
from .views import user_login, registers_new_user, confirm_new_user_registration,edit_user_profile

app_name = 'authapp'

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('register/', registers_new_user, name='registers_new_user'),
    path('edit/', edit_user_profile, name='edit_user_profile'),
    path('confirm_registration/<email>/<activation_key>', confirm_new_user_registration,
         name='confirm_new_user_registration')

]
