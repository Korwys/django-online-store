from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import PermissionDenied

from orderapp.models import Order
from .permissions import AdminOnly
from .serializers import ProductSerializer, BrandSerializer, CategorySerializer, GenderSerializer, OrderSerializer
from productapp.models import Product, Brand, ProductCategory, Genders


class ProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'price']


class RetrieveProductAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class RetrieveUpdateDestroyProductAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    permission_classes = (AdminOnly,)


class BrandAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class RetrieveBrandAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'id'


class RetrieveUpdateDestroyBrandAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'id'
    permission_classes = (AdminOnly,)


class CategoryAPIView(ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer


class RetrieveCategoryAPIView(RetrieveAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class RetrieveUpdateDestroyCategoryAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'
    permission_classes = (AdminOnly,)


class GenderAPIView(ListAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializer


class RetrieveGenderAPIView(RetrieveAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializer
    lookup_field = 'id'


class RetrieveUpdateDestroyGenderAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializer
    lookup_field = 'id'
    permission_classes = (AdminOnly,)


class OrderListAPIView(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            raise PermissionDenied(detail='Вы не вошли в личный кабинет')
        else:
            return Order.objects.filter(user=user)


class RetrieveOrderAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
