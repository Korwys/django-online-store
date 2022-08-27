from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from cartapp.models import Cart
from cartapp.services.crud import  add_selected_product_in_cart, change_product_quantity, \
    remove_selected_product_from_cart
from orderapp.models import Order
from orderapp.services.crud import change_order_status, transfer_products_from_cart_to_orderitem
from wishapp.models import WishList
from wishapp.services.crud import save_selected_product, remove_selected_product
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
        pk = kwargs['id']
        change_order_status(pk)
        return Response(status=status.HTTP_200_OK, data={'message': 'Заказ удален'})


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        new_user_order = Order.objects.create(
            user=user,
            city=request.POST.get('city'),
            address=request.POST.get('address'),
            postal_code=request.POST.get('postal_code'),
            status='PD',
            is_active=True,
        )

        transfer_products_from_cart_to_orderitem(request, new_user_order)
        return Response(status=status.HTTP_200_OK, data={'message': 'Заказ создан'})


class WishListAPIView(ListAPIView):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            raise PermissionDenied(detail='Вы не вошли в личный кабинет')
        else:
            return WishList.objects.filter(user=user)


class WishlistAddAPIView(CreateAPIView):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        pk = kwargs['id']
        save_selected_product(request, pk)

        return Response(status=status.HTTP_200_OK, data={'message': 'Товар добавлен в избранное'})


class WishlistDeleteItemAPIView(DestroyAPIView):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated, ]

    def delete(self, request, *args, **kwargs):
        pk = kwargs['id']
        remove_selected_product(pk)

        return Response(status=status.HTTP_200_OK, data={'message': 'Товар удален из избранного'})


class CartListAPIView(ListAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            raise PermissionDenied(detail='Вы не вошли в личный кабинет')
        else:
            return Cart.objects.filter(user=user)


class CartAddAPIView(CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        pk = kwargs['id']
        add_selected_product_in_cart(request, pk)
        return Response(status=status.HTTP_200_OK, data={'message': 'Товар добавлен в корзину'})


class CartUpdateAPIView(UpdateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, ]

    def put(self, request, *args, **kwargs):
        pk = kwargs['id']
        quantity = kwargs['quantity']
        change_product_quantity(request, pk, quantity)


class CartDeleteAPIView(DestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, ]

    def delete(self, request, *args, **kwargs):
        pk = kwargs['id']
        remove_selected_product_from_cart(pk)
        return Response(status=status.HTTP_200_OK, data={'message': 'Товар удален из корзины'})
