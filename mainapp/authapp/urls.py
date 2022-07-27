from django.urls import path
from .views import user_login, new_user_registration, confirm_new_user_registration

app_name = 'authapp'

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('register/', new_user_registration, name='new_user_registration'),
    path('confirm_registration/<email>/<activation_key>', confirm_new_user_registration,
         name='confirm_new_user_registration')

]
