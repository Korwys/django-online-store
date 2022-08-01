from django.contrib import admin

from wishapp.models import WishList


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    pass
