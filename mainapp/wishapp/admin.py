from django.contrib import admin

from wishapp.models import WishList


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'created_at']
    search_fields = ['user']
