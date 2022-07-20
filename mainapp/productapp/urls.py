from django.urls import path
from .views import products, category,single_product

app_name = 'productapp'
urlpatterns = [
    path('', products, name='products'),
    path('gender/<int:pk>/', products, name='gender'),
    path('category/<int:pk>/', category, name='category'),
    path('single-product/<int:pk>', single_product, name='single_product'),

]
