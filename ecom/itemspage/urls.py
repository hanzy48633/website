from django.urls import path
from .views import index, productDetail


urlpatterns = [
    path('', index, name='index_view'),
    path('<int:_id>/', productDetail, name='product_view')
]