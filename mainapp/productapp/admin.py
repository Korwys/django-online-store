from django.contrib import admin

from .models import ProductCategory, Product, Gallery, Genders


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Genders)
class GendersAdmin(admin.ModelAdmin):
    pass


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline]
