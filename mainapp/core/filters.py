import django_filters

from productapp.models import Product


class ProductFilter(django_filters.FilterSet):
    """Фильтр товаров по бренду, категории,полу"""

    class Meta:
        model = Product
        fields = ['brand','category','gender']