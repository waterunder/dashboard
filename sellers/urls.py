from django.urls import path

from .views import SellerDetailView, SellerListView

urlpatterns = [
    path('', SellerListView.as_view(), name='seller_list'),
    path('<uuid:pk>', SellerDetailView.as_view(), name='seller_detail'),
]
