from django.urls import path
from .views import products, single_product_page, filter_by_gender, filter_by_category

app_name = 'productapp'
urlpatterns = [
    path('', products, name='products'),
    path('gender/<int:pk>/', filter_by_gender, name='gender'),
    path('category/<int:pk>/', filter_by_category, name='category'),
    path('single-product/<int:pk>', single_product_page, name='single_product'),

]
