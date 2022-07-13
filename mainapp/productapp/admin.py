from django.contrib import admin

from .models import ProductCategory, Product, Gallery, Genders

admin.site.register(ProductCategory)



class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline]

admin.site.register(Genders)