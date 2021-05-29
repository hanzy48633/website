from django.urls import path
from .views import index, productDetail, login


urlpatterns = [
    path('', index, name='index_view'),
    path('<int:_id>/', productDetail, name='product_view'),
    path('login', login, name='login_view'),
]