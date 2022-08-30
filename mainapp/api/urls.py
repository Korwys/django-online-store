from django.urls import path, include
from rest_framework import routers

from .views import BrandAPIView, CategoryAPIView, GenderAPIView, OrderListAPIView, ProductAPIView, \
    OrderCancelAPIView, OrderCreateAPIView, WishListAPIView, WishlistDeleteItemAPIView, WishlistAddAPIView, \
    CartListAPIView, CartAddAPIView, CartUpdateAPIView, CartDeleteAPIView

app_name = 'api'

router = routers.DefaultRouter()
router.register('products', ProductAPIView)
router.register('brands', BrandAPIView)
router.register('categories', CategoryAPIView)
router.register('genders', GenderAPIView)

urlpatterns = [
    path('', include(router.urls)),


    path('orders/', OrderListAPIView.as_view()),
    path('orders/delete/<int:id>', OrderCancelAPIView.as_view()),
    path('orders/create/', OrderCreateAPIView.as_view()),

    path('wishlists/', WishListAPIView.as_view()),
    path('wishlists/delete/<int:id>', WishlistDeleteItemAPIView.as_view()),
    path('wishlists/add/<int:id>', WishlistAddAPIView.as_view()),

    path('carts/', CartListAPIView.as_view()),
    path('carts/add/<int:id>', CartAddAPIView.as_view()),
    path('carts/update/<int:id>/<int:quantity>', CartUpdateAPIView.as_view()),
    path('carts/delete/<int:id>', CartDeleteAPIView.as_view())

]
