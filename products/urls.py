from django.urls import path

from .views import (ProductCreate, ProductDetailView, ProductListView,
                    SellerProductList)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<uuid:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<seller>/', SellerProductList.as_view(), name='seller_product_list'),
]
