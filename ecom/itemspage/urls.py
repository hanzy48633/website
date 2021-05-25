from django.urls import path
from .views import index, productDetail


urlpatterns = [
    path('', index, name='index-view'),
    path('<int:_id>/', productDetail, name='product-view')
]