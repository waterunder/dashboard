import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seller = self.get_object()
        context['seller_products'] = seller.products.all()
        return context


class SellerCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Seller
    fields = ['name', 'description', 'email', 'address1', 'address2', 'zip_code',
              'city', 'country', 'logo', 'header_image', ]
    success_message = "%(name)s was created successfully!"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        logger.info('seller owner %s', form.instance.owner)
        return super().form_valid(form)


class SellerUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Seller
    fields = ['name', 'description', 'email', 'address1', 'address2', 'zip_code',
              'city', 'country', 'logo', 'header_image', ]

    template_name_suffix = '_update_form'
    success_message = "%(name)s was updated successfully!"


class SellerDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Seller
    success_url = reverse_lazy('dashboard')
    success_message = "Seller was deleted successfully!"

    def delete(self, request, *args, **kwargs):
        if not self.get_object().can_delete(self.request.user):
            logger.critical('Possible Hack attack: user %s, obj: %s',
                            self.request.user, self.get_object())
            return HttpResponse('Unauthorized', status=401)
        messages.success(self.request, self.success_message)
        return super(SellerDelete, self).delete(request, *args, **kwargs)
