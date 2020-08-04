from django.views.generic import DetailView, ListView

from sellers.models import Seller


class SellerListView(ListView):
    model = Seller
    context_object_name = 'seller_list'
    template = 'sellers/seller_list.html'


class SellerDetailView(DetailView):
    model = Seller
    context_object_name = 'seller'
    template = 'sellers/seller_detail.html'
