from django.contrib import admin

from .models import ProductCategory, Product, Gallery

admin.site.register(ProductCategory)



class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline]
