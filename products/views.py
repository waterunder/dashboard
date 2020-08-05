import logging

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from products.models import Product
from sellers.models import Seller

logger = logging.getLogger(__name__)


class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'


class SellerProductList(ListView):
    template_name = 'products/products_by_seller.html'

    def get_queryset(self):
        self.seller = get_object_or_404(Seller, name=self.kwargs['seller'])
        return Product.objects.filter(seller=self.seller)

    def get_context_data(self, **kwargs):
        # call the base context first
        context = super().get_context_data(**kwargs)
        context['seller'] = self.seller
        return context


class ProductCreate(CreateView):
    model = Product
    fields = ['title', 'price']
