from django.urls import path

from .views import ProductAPIView, BrandAPIView, CategoryAPIView, GenderAPIView, RetrieveProductAPIView, \
    RetrieveUpdateDestroyProductAPIView, RetrieveBrandAPIView, RetrieveUpdateDestroyBrandAPIView, \
    RetrieveUpdateDestroyCategoryAPIView, RetrieveCategoryAPIView, RetrieveGenderAPIView, \
    RetrieveUpdateDestroyGenderAPIView, OrderListAPIView, RetrieveOrderAPIView

app_name = 'api'

urlpatterns = [
    path('productlist/', ProductAPIView.as_view()),
    path('product/<int:id>', RetrieveProductAPIView.as_view()),
    path('productupdate/<int:id>', RetrieveUpdateDestroyProductAPIView.as_view()),

    path('brandlist/', BrandAPIView.as_view()),
    path('brand/<int:id>', RetrieveBrandAPIView.as_view()),
    path('brandupdate/<int:id>', RetrieveUpdateDestroyBrandAPIView.as_view()),

    path('categorylist/', CategoryAPIView.as_view()),
    path('category/<int:id>', RetrieveCategoryAPIView.as_view()),
    path('categoryupdate/<int:id>', RetrieveUpdateDestroyCategoryAPIView.as_view()),

    path('genderlist/', GenderAPIView.as_view()),
    path('gender/<int:id>', RetrieveGenderAPIView.as_view()),
    path('genderupdate/<int:id>', RetrieveUpdateDestroyGenderAPIView.as_view()),

    path('orderlist/', OrderListAPIView.as_view()),
    path('order/<int:id>', RetrieveOrderAPIView.as_view())
]
