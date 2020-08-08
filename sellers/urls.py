from django.urls import path

from .views import SellerCreate, SellerDetailView, SellerListView

urlpatterns = [
    path('', SellerListView.as_view(), name='seller_list'),
    path('<uuid:pk>', SellerDetailView.as_view(), name='seller_detail'),
    path('create/', SellerCreate.as_view(), name='seller_create'),
]
