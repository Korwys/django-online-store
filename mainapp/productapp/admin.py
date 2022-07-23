from django.contrib import admin

from .models import ProductCategory, Product, Gallery, Genders

admin.site.register(ProductCategory)
admin.site.register(Genders)



class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline]

