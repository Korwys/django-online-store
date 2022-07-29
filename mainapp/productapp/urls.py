from django.urls import path
from .views import get_all_products, get_single_product_page, get_products_by_gender, get_products_by_category

app_name = 'productapp'
urlpatterns = [
    path('', get_all_products, name='products'),
    path('gender/<int:pk>/', get_products_by_gender, name='gender'),
    path('category/<int:pk>/', get_products_by_category, name='category'),
    path('single-product/<int:pk>', get_single_product_page, name='single_product'),

]
