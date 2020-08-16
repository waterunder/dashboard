import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

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


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['title', 'description', 'price', 'active', 'in_stock', 'tags']

    def form_valid(self, form):
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['title', 'description', 'price', 'active', 'in_stock', 'tags']
    template_name_suffix = '_update_form'


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


class SearchResultsListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        logger.info('processing search query=%s...', query)
        return Product.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
