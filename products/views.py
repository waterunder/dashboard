from django.views.generic import DetailView, ListView

from .models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'dashboard/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'dashboard/product_detail.html'
