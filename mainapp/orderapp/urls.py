from django.urls import path

from orderapp.views import get_all_user_orders_view, create_user_order_view, cancel_user_order_view

app_name = 'orderapp'

urlpatterns = [
    path('', get_all_user_orders_view, name='orders'),
    path('create/', create_user_order_view, name='create_order'),
    path('remove/<int:pk>', cancel_user_order_view, name='cancel_order'),

]
