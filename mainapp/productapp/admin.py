from django.contrib import admin

from .models import ProductCategory, Product, Gallery, Genders, Brand


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_active', 'image']
    list_editable = ['description', 'is_active', 'image']
    ordering = ['name']
    list_per_page = 10
    search_fields = ['name']


@admin.register(Genders)
class GendersAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'image']
    list_editable = ['is_active', 'image']
    search_fields = ['name']


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


class PriceFilter(admin.SimpleListFilter):
    title = 'Filter'
    parameter_name = 'filter'

    def lookups(self, request, model_admin):
        return [
            ('<1000', '<1000'),
            ('1000-5000', '1000-5000'),
            ('5000-10000', '5000-10000'),
            ('10000-20000', '10000-20000'),
            ('20000+', '20000+'),
        ]

    def queryset(self, request, queryset):
        """"Фильтрует товары по цене"""
        if self.value() == '<1000':
            return queryset.filter(price__lt=1000)
        if self.value() == '1000-5000':
            return queryset.filter(price__gte=1000).filter(price__lte=5000)
        if self.value() == '5000-10000':
            return queryset.filter(price__gte=5000).filter(price__lte=10000)
        if self.value() == '10000-20000':
            return queryset.filter(price__gte=10000).filter(price__lte=20000)
        if self.value() == '20000+':
            return queryset.filter(price__gte=20000)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'brand', 'price']
    list_editable = ['category', 'brand', 'price', ]
    ordering = ['price', 'name']
    list_per_page = 8
    inlines = [GalleryInline]
    search_fields = ['name']
    list_filter = ['brand', PriceFilter]
