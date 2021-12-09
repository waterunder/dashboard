from django.urls import path

from .views import (
    SellerCreate,
    SellerDelete,
    SellerDetailView,
    SellerListView,
    SellerUpdate,
)

urlpatterns = [
    path('', SellerListView.as_view(), name='seller_list'),
    path('<uuid:pk>', SellerDetailView.as_view(), name='seller_detail'),
    path('create/', SellerCreate.as_view(), name='seller_create'),
    path('<uuid:pk>/update/', SellerUpdate.as_view(), name='seller_update'),
    path('<uuid:pk>/delete/', SellerDelete.as_view(), name='seller_delete'),
]
