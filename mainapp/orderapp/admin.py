from django.contrib import admin

from orderapp.models import OrderItem, Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','city', 'address', 'postal_code', 'status','created_at','updated_at']
    list_editable = ['city', 'address', 'postal_code', 'status']
    list_per_page = 10


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity']
    list_editable = ['product', 'quantity']