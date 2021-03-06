from django.urls import path

from products.views import (
    ProductCreate,
    ProductDelete,
    ProductDetailView,
    ProductListView,
    ProductUpdate,
    SearchResultsListView,
    SellerProductList,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('<uuid:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<uuid:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('<uuid:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('<seller>/', SellerProductList.as_view(), name='seller_product_list'),
]
