import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from products.models import Product
from sellers.models import Seller

logger = logging.getLogger(__name__)


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 8
    context_object_name = 'product_list'
    template_name = 'products/product_list.html'
    login_url = 'account_login'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'
    login_url = 'account_login'


class SellerProductList(LoginRequiredMixin, ListView):
    template_name = 'products/products_by_seller.html'
    paginate_by = 8
    login_url = 'account_login'

    def get_queryset(self):
        self.seller = get_object_or_404(Seller, name=self.kwargs['seller'])
        return Product.objects.filter(seller=self.seller)

    def get_context_data(self, **kwargs):
        # call the base context first
        context = super().get_context_data(**kwargs)
        context['seller'] = self.seller
        return context


class ProductCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    fields = ['title', 'description', 'price', 'active', 'in_stock', 'tags']
    success_message = "%(title)s was created successfully!"

    def form_valid(self, form):
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)


class ProductUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    fields = ['title', 'description', 'price', 'active', 'in_stock', 'tags']
    template_name_suffix = '_update_form'
    success_message = "%(title)s was updated successfully!"

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.seller.owner == self.request.user:
            logger.critical('Possible attack: \nuser: %s\nobj: %s', self.request.user, obj)
            raise Http404
        return obj


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
    success_message = "Product was deleted successfully!"

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.seller.owner == self.request.user:
            logger.critical('Possible attack: \nuser: %s\nobj: %s', self.request.user, obj)
            raise Http404
        return obj

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ProductDelete, self).delete(request, *args, **kwargs)


class SearchResultsListView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 8
    context_object_name = 'product_list'
    template_name = 'products/search_results.html'
    login_url = 'account_login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
