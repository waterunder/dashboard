from dive.models import Dive
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView


class DiveListView(LoginRequiredMixin, ListView):
    model = Dive
    context_object_name = 'dive_list'
    template_name = 'dive/dive_list.html'


class DiveDetailView(LoginRequiredMixin, DetailView):
    model = Dive
    context_object_name = 'dive'
    template_name = 'dive/dive_detail.html'
