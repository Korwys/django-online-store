from django.urls import path
from .views import index

app_name = 'productapp'
urlpatterns = [
    path('',index, name='index'),
]