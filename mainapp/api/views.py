from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView, \
    CreateAPIView
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils.timezone import now

from cartapp.models import Cart
from cartapp.services.crud import get_cart_products_by_user
from orderapp.models import Order, OrderItem
from wishapp.models import WishList
from .permissions import IsStaffOrReadOnly
from .serializers import ProductSerializer, BrandSerializer, CategorySerializer, GenderSerializer, OrderSerializer, \
    WishlistSerializer, CartSerializer
from productapp.models import Product, Brand, ProductCategory, Genders


class ProductAPIView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'price']
    permission_classes = [IsStaffOrReadOnly, ]


class BrandAPIView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    permission_classes = [IsStaffOrReadOnly, ]


class CategoryAPIView(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']
    permission_classes = [IsStaffOrReadOnly, ]


class GenderAPIView(ModelViewSet):
    queryset = Genders.objects.all()
    serializer_class = GenderSerializer
    permission_classes = [IsStaffOrReadOnly, ]


class OrderListAPIView(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            raise PermissionDenied(detail='Вы не вошли в личный кабинет')
        else:
            return Order.objects.filter(user=user)


class OrderCancelAPIView(DestroyAPIView):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        user_orders = Order.objects.filter(user=user)
        select_user_order = get_object_or_404(user_orders, pk=kwargs['id'])
        select_user_order.status = 'CNL'
        select_user_order.is_active = False
        select_user_order.save()
        return Response(status=status.HTTP_200_OK, data={'message': 'Заказ удален'})


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()

    def post(self, request, *args, **kwargs):
        user = self.request.user
        new_user_order = Order.objects.create(
            user=user,
            city=request.POST.get('city'),
            address=request.POST.get('address'),
            postal_code=request.POST.get('postal_code'),
            status='PD',
            is_active=True,
            created_at= now(),
            updated_at=now(),
        )

        cart = get_cart_products_by_user(request)
        for item in cart:
            OrderItem.objects.create(order=new_user_order, product=item.product, quantity=item.quantity)
        cart.delete()
        return Response(status=status.HTTP_200_OK, data={'message': 'Заказ создан'})




