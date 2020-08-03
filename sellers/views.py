from django.views.generic import DetailView, ListView

from .models import Seller


class SellerListView(ListView):
    model = Seller
    context_object_name = 'seller_list'
    template = 'dashboard/seller_list.html'


class SellerDetailView(DetailView):
    model = Seller
    context_object_name = 'seller'
    template = 'sellers/seller_detail.html'
