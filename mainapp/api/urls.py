from django.urls import path, include
from rest_framework import routers

from .views import BrandAPIView, CategoryAPIView, GenderAPIView, OrderListAPIView, ProductAPIView, \
    OrderCancelAPIView, OrderCreateAPIView

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
    path('orders/create/', OrderCreateAPIView.as_view())

]
