from django.contrib import admin
from django.urls import path, include
from .views import index, contacts, about



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('products/', include('productapp.urls', namespace='products')),

]
