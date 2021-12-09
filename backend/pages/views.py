from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin
from pages import forms


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactUsView(SuccessMessageMixin, FormView):
    template_name = 'contact_form.html'
    form_class = forms.ContactForm
    success_message = 'Message sent successfully!'
    success_url = '/'

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)
