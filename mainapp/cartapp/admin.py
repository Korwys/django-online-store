from django.contrib import admin

from cartapp.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass
