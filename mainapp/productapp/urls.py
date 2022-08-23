from django.urls import path
from .views import get_all_products, get_single_product_page

app_name = 'productapp'
urlpatterns = [

    path('', get_all_products, name='products'),
    path('single-product/<int:pk>', get_single_product_page, name='single_product'),

]
