from django.urls import path
from .views import login

app_name = 'authapp'
urlpatterns = [
    path('login/', login, name='login')

]
