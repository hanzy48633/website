from django.urls import path
from .views import index, productDetail, _login, register, _logout


urlpatterns = [
    path('', index, name='index_view'),
    path('<int:_id>/', productDetail, name='product_view'),
    path('login', _login, name='login_view'),
    path('logout', _logout, name='logout_view'),
    path('register', register, name='register_view'),
]