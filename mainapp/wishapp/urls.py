from django.urls import path

from wishapp.views import get_all_user_wishlist_products, add_product_in_wishlist, remove_product_from_wishlist

app_name = 'wishapp'

urlpatterns = [
    path('', get_all_user_wishlist_products, name='wishlist'),
    path('add/<int:pk>', add_product_in_wishlist, name='add_in_wishlist'),
    path('remove/<int:pk>', remove_product_from_wishlist, name='remove_from_wishlist')

]
