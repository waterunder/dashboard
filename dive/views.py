import logging

from dive.models import Dive
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

logger = logging.getLogger(__name__)


class DiveListView(LoginRequiredMixin, ListView):
    model = Dive
    context_object_name = 'dive_list'
    template_name = 'dive/dive_list.html'


class DiveDetailView(LoginRequiredMixin, DetailView):
    model = Dive
    context_object_name = 'dive'
    template_name = 'dive/dive_detail.html'


class DiveCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Dive
    fields = ['date', 'lat', 'lon', 'visibility', 'bottom_time', 'description']
    success_message = "Dive was created successfully!"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DiveUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Dive
    fields = ['date', 'lat', 'lon', 'visibility', 'bottom_time', 'description']
    success_message = "Dive was updated successfully!"


class DiveDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Dive
    success_url = reverse_lazy('dive_list')
    success_message = "Dive was deleted successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DiveDelete, self).delete(request, *args, **kwargs)
