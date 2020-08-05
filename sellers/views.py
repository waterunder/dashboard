import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from sellers.models import Seller

logger = logging.getLogger(__name__)


class SellerListView(LoginRequiredMixin, ListView):
    model = Seller
    context_object_name = 'seller_list'
    template = 'sellers/seller_list.html'


class SellerDetailView(LoginRequiredMixin, DetailView):
    model = Seller
    context_object_name = 'seller'
    template = 'sellers/seller_detail.html'


class SellerCreate(LoginRequiredMixin, CreateView):
    model = Seller
    fields = ['name', 'description', 'email', 'address1', 'address2', 'zip_code',
              'city', 'country', 'logo', 'header_image', ]
    logger.info('inside seller create...')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        logger.info('seller owner %s', form.instance.owner)
        return super().form_valid(form)
