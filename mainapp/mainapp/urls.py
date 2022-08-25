from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

from .views import index, contacts, about
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('api/v1/', include('api.urls', namespace='api')),
    path('products/', include('productapp.urls', namespace='products')),
    path('cart/', include('cartapp.urls', namespace='cart')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('wishlist/', include('wishapp.urls', namespace='wishlist')),
    path('order/', include('orderapp.urls', namespace='order')),
    path('', include('social_django.urls', namespace='social')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [re_path(r'^__debug__/', include(debug_toolbar.urls))]
