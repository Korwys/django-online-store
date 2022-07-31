from django.urls import path

from cartapp.views import get_user_cart, add_product_in_cart, remove_product_from_cart, edit_user_cart

app_name = 'cartapp'

urlpatterns = [
    path('', get_user_cart, name='get_user_cart'),
    path('add/<int:pk>', add_product_in_cart, name='add_product_in_cart'),
    path('remove/<int:pk>', remove_product_from_cart, name='remove_product_from_cart'),
    path('edit/<int:pk>/<int:quantity>/', edit_user_cart, name='edit_user_cart')
]
